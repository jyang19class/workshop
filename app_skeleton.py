from flask import Flask, request, Response
from flask_cors import CORS
from database.db import initialize_db
from database.models import Note

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}

initialize_db(app)

@app.route('/')
def root():
    return 

@app.route('/getall')
def getAll():

    return 

@app.route('/get/<noteId>')
def get(noteId):
    
    return 


@app.route('/add', methods=['POST'])
def post():
    

    return 

@app.route('/change/<noteId>', methods=['PUT'])
def put(noteId):
    

    return 

@app.route('/change/<noteId>', methods=['DELETE'])
def delete(noteId):
    
    return 


app.run()