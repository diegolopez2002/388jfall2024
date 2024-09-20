from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm
from bson.objectid import ObjectId

uri = ""
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    app = Flask(__name__)
    app.config["MONGO_URI"] = ""
    mongo = PyMongo(app)
    client.admin.command('ping')
    new_post = {
                'user': 'form.user.data',
                'text': 'form.text.data'}
    mongo.db.posts.insert_one(new_post)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)