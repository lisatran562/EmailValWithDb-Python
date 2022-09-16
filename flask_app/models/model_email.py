# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * from emails;"
        results = connectToMySQL(DB).query_db(query)

        all_emails = []
        for email in results:
            all_emails.append(cls(email))
        return all_emails


    @staticmethod
    def validate(email) -> bool:
        is_valid = True

        if EMAIL_REGEX.match(email['email']):
            is_valid = True
            flash("The email address you entered is a VALID email address!  Thank you!", 'success_user_email')
        else:
            flash("Invalid email.", 'err_user_email')
            is_valid = False

        return is_valid






        