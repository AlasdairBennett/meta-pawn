# meta-pawn

Chess metagame statistics explorer<br>
<br>
<br>
Term project for COSC4427<br>
<br>
This project uses [this dataset](https://www.kaggle.com/datasnaek/chess) <br>

<h2>Installation Directions:</h2>
Requires python 3.9.5<br>

From the project directory, run the following command to create a virtual environment:<br>
`python3 -m venv venv`
<br>

Run the activate script:<br>
`venv/Scripts/activate.bat`<br>

Install the required packages for the project:<br>
`pip install -r requirements.txt`<br>

Configure the environment variables:<br>
`set FLASK_APP=app.py`<br>
`set FLASK_ENV=development`<br>

Run the app:<br>
`flask run`<br>

Navigate to `127.0.0.1:5000` 