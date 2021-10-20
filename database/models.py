from enum import unique
from .db import db

class Note(db.Document):
    noteId = db.LongField(required=True, unique=True)
    title = db.StringField(required=True)
    body = db.StringField(required=True)

