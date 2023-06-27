from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_bcrypt import Bcrypt
import pprint
bcrypt = Bcrypt(app)
import re
import pickle


class LTG:
    db = "vision_board"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.goal_date = data['goal_date']
        self.is_complete = data['is_complete']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.stg = []

    @classmethod
    def create_long_term_goal(cls, data, file):
        if not cls.ltg_goal_validations(data):
            return False
        good_data = cls.parce_ltg_data(data, file)
        query = """
                INSERT INTO long_term_goals (title, description, goal_date, is_complete, image, user_id)
                VALUES (%(title)s, %(description)s, %(goal_date)s, %(is_complete)s, %(image)s, %(user_id)s)
                """
        results = connectToMySQL(cls.db).query_db(query, good_data)
        pprint.pp(results)
        return results

#* Validations for Long Term Goals
    @staticmethod
    def ltg_goal_validations(data):
        is_valid = True
        if len(data['title']) <= 2:
            flash('Title must be at least 2 characters long')
            is_valid = False
        if len(data['description']) <= 3:
            flash('Description must be at least 3 characters long')
            is_valid = False
        if data['is_complete'] == "Yes" or data['is_complete'] == "No":
            print("Is_complete should be good", data['is_complete'])
        else:
            flash("Completion can only be either 'Yes' or 'No'")
            is_valid = False
        return is_valid
    
    @staticmethod
    def parce_ltg_data(form_data, filename):
        print("Parced File Name: ", filename)
        parced_data = {}
        parced_data['title'] = form_data['title']
        parced_data['description'] = form_data['description']
        parced_data['goal_date'] = form_data['goal_date']
        parced_data['is_complete'] = form_data['is_complete']
        parced_data['image'] = filename
        parced_data['user_id'] = form_data['user_id']
        return parced_data