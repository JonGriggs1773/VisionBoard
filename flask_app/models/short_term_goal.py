from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_bcrypt import Bcrypt
import pprint
bcrypt = Bcrypt(app)
import re


class STG:
    db = "vision_board"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.goal_date = data['goal_date']
        self.is_complete = data['is_complete']
        self.user_id = data['user_id']
        self.long_term_goal_id = data['long_term_goal_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.ltg = None
        self.tasks = []


    @classmethod
    def create_short_term_goal(cls, data):
        if not cls.short_term_goal_validations(data):
            return False
        good_data = cls.parce_stg_data(data)
        query = """
                INSERT INTO short_term_goals (title, description, goal_date, is_complete, user_id, long_term_goal_id)
                VALUES (%(title)s, %(description)s, %(goal_date)s, %(is_complete)s, %(user_id)s, %(long_term_goal_id)s)
                """
        results = connectToMySQL(cls.db).query_db(query, good_data)
        pprint.pp(results)
        return results
    
    #* Validations for Short Term Goals
    @staticmethod
    def short_term_goal_validations(data):
        is_valid = True
        if len(data['title']) <= 2:
            flash('Title must be at least 2 characters long')
            is_valid = False
        if len(data['description']) <= 3:
            flash('Description must be at least 3 characters long')
            is_valid = False
        if not data['goal_date']:
            flash('Goal date must be a valid date')
            is_valid = False
        return is_valid
    
    @staticmethod
    def parce_stg_data(data):
        parced_data = {}
        parced_data['title'] = data['title']
        parced_data['description'] = data['description']
        parced_data['goal_date'] = data['goal_date']
        parced_data['is_complete'] = data['is_complete']
        parced_data['user_id'] = data['user_id']
        parced_data['long_term_goal_id'] = data['long_term_goal_id']
        return parced_data