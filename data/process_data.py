import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Loads data from gaven files

    Args:
        messages_filepath: path for messages
        categories_filepath: Path for categories

    Returns:
        df:Merged dataset
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on="id")
    return df


def clean_data(df):
    """
    Clean data

    Args:
       source dataset

    Returns:
        df:cleaned dataset
    """
    categories = df["categories"].str.split(";", expand=True)
    row = categories.loc[0]
    category_colnames = row.apply(lambda x: x.split('-')[0])
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(
            lambda x: x.split('-')[1] if int(x.split('-')[1]) < 2 else 1)
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    # drop the original categories column from `df`
    df.drop("categories", axis=1, inplace=True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    # drop duplicates
    df = df.drop_duplicates(keep='first')
    return df


def save_data(df, database_filename):
    """
    sage data to database 

    Args:
        df:dataset
        database_filename:data base file name
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('cleanData', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[
            1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'.format(
            messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '
              'datasets as the first and second argument respectively, as '
              'well as the filepath of the database to save the cleaned data '
              'to as the third argument. \n\nExample: python process_data.py '
              'disaster_messages.csv disaster_categories.csv '
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
