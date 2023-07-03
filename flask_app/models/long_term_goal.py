from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.short_term_goal import STG
from flask import flash, session
from flask_bcrypt import Bcrypt
import pprint
bcrypt = Bcrypt(app)


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
    
    @classmethod
    def get_ltg_by_id(cls,id):
        data = {"id":id}
        query = """
                SELECT *
                FROM long_term_goals
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        pprint.pp(results)
        ltg = cls(results[0])
        return ltg
    
    @classmethod
    def get_ltg_with_all_stgs(cls, id):
        data = {'id': id}
        query = """
                SELECT *
                FROM long_term_goals
                LEFT JOIN short_term_goals
                ON long_term_goals.id = short_term_goals.long_term_goal_id
                WHERE long_term_goals.id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        pprint.pp(results)
        if results:
            ltg = cls(results[0])
            for stg in results:
                stg_data = {
                    'id': stg['short_term_goals.id'],
                    'title': stg['title'],
                    'description': stg['description'],
                    'goal_date': stg['goal_date'],
                    'is_complete': stg['is_complete'],
                    'user_id': stg['user_id'],
                    'long_term_goal_id': stg['long_term_goal_id'],
                    'created_at': stg['short_term_goals.created_at'],
                    'updated_at': stg['short_term_goals.updated_at']
                }
                ltg.stg.append(STG(stg_data))
            return ltg
        else:
            print("Results were empty bro! Figure it out!")
            return False
        
    @classmethod
    def delete_ltg_by_id(cls, id):
        data = {'id': id}
        query = """
                DELETE
                FROM long_term_goals
                WHERE id = %(id)s
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

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