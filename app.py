from flask import Flask, render_template
import db

app = Flask(__name__)



@app.route("/")
def initial():
    return render_template('index.html')

#test to insert data to the data base
@app.route("/thepiecluster")
def thepiecluster():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"


if __name__ == '__main__':
    	app.run( # Starts the site
		host='0.0.0.0', port=8000 )