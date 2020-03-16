# Udacity_Pro2
# Disaster Response Pipeline Project

Portfolio project to showcase Data Engineering skills including ETL and ML Pipeline preparation, utilising model in a web app, and data visualisation.

This project is to use the data engineering skills to do a message classification function, the totally process is that ETL pipeline -> ML pipeline -> Flask 

### How to run it:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and save the model
        `python model/train_classifier.py data/ETLFinal.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

