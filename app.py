from flask import Flask, request, Response

from database.db import initialize_db
from database.models import Note

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}

initialize_db(app)

@app.route('/')
def hello():
    return {'hello': 'world'}

@app.route('/get/<noteId>')
def get(noteId):
    note = Note.objects.get(noteId=noteId).to_json()
    return note, 200


@app.route('/add', methods=['POST'])
def post():
    body = request.get_json()
    Note(**body).save()
    return '', 200

@app.route('/put/<noteId>', methods=['PUT'])
def put(noteId):
    body = request.get_json()
    Note.objects.get(noteId=noteId).update(**body)
    return '', 200

@app.route('/delete/<noteId>', methods=['DELETE'])
def delete(noteId):
    Note.objects.get(noteId=noteId).delete()
    return '', 200


app.run()