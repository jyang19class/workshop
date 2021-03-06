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
    return "Hello World"

@app.route('/getall')
def getAll():
    all = Note.objects.to_json()
    return Response(all, status=200)


@app.route('/get/<noteId>')
def get(noteId):
    note = Note.objects.get(noteId=noteId).to_json()
    return Response(note, mimetype="application/json", status=200)


@app.route('/add', methods=['POST'])
def post():
    body = request.get_json()
    Note(**body).save()
    return '', 200

@app.route('/change/<noteId>', methods=['PUT'])
def put(noteId):
    try:
        body = request.get_json()
        Note.objects.get(noteId=noteId).update(**body)
        return '', 200
    except Note.DoesNotExist:
        return "Note not found", 404

@app.route('/change/<noteId>', methods=['DELETE'])
def delete(noteId):
    Note.objects.get(noteId=noteId).delete()
    return '', 200


app.run()