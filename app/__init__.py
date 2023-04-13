"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq57pmbg5e4khqo8rg-a.oregon-postgres.render.com",
        database="maitodo",
        user="maitodo_user",
        password="MhIhVn6rWBexybeHMALJKIQDxQumQ0hS")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
