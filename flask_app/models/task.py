from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_bcrypt import Bcrypt
import pprint
bcrypt = Bcrypt(app)


class Task:
    
    db = "vision_board"
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.goal_date = data['goal_date']
        self.is_complete = data['is_complete']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.stg = None
        self.user = None
        
    
    @classmethod
    def add_task(cls, data):
        if not cls.validate_task(data):
            return False
        else:
            query = """
                    INSERT INTO tasks (title, description, goal_date, is_complete, user_id, short_term_goal_id)
                    VALUES (%(title)s, %(description)s, %(goal_date)s, %(is_complete)s, %(user_id)s, %(short_term_goal_id)s)
                    """
                    
            result = connectToMySQL(cls.db).query_db(data, query)
            pprint.pp(result)
            return result
    
    
    @staticmethod
    def validate_task(data):
        is_valid = True
        if len(data['title']) <= 2:
            flash('Title must be at least 2 characters long')
            is_valid = False
        if len(data['description']) <= 3:
            flash('Description must be at least 3 characters long')
            is_valid = False
            
        return is_valid
        

