from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.long_term_goal import LTG
from flask import flash, session
from flask_bcrypt import Bcrypt
import pprint
bcrypt = Bcrypt(app)
import re
#! To get these comments color coded, download the "Better Comments" extention in VS Code



class User:
    db = 'vision_board'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.short_term_goals = []
        self.long_term_goals = []

    #? Assigning user in database and putting user id and full name in session
    @classmethod
    def create_user(cls, data):
        if not cls.validate_user(data):
            return False
        data = cls.parse_user_data(data)
        query = """  
                INSERT INTO users (first_name, last_name, username, email, password)
                VALUES(%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s)
                """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        session['user_id'] = user_id
        session['user_name'] = f"{data['first_name']} {data['last_name']}"
        return True
    
    @classmethod
    def get_user_by_email(cls, email):
        data = {'email': email}
        query = """
                SELECT * FROM users
                WHERE email = %(email)s
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result
    
    @classmethod
    def get_user_by_id(cls, id):
        data = {'id': id}
        query = """
                SELECT * FROM users
                WHERE id = %(id)s
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        pprint.pp(result)
        if result:
            user = cls(result[0])
            return user
        else:
            return result
    
    @classmethod
    def get_user_by_username(cls, username):
        data = {'username': username}
        query = """
                SELECT * FROM users
                WHERE username = %(username)s
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result
    
    @classmethod
    def get_user_with_ltgs_by_user_id(cls, id):
        data = {'id': id}
        query = """
                SELECT * FROM users 
                LEFT JOIN long_term_goals
                ON users.id = long_term_goals.user_id
                WHERE users.id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        pprint.pp(results)
        one_user = cls(results[0])
        for ltg in results:
            ltg_data = {
                'id': ltg['long_term_goals.id'],
                'title': ltg['title'],
                'description': ltg['description'],
                'goal_date': ltg['goal_date'],
                'is_complete': ltg['is_complete'],
                'image': ltg['image'],
                'user_id': ltg['user_id'],
                'created_at': ltg['long_term_goals.created_at'],
                'updated_at': ltg['long_term_goals.updated_at']
            }
            one_user.long_term_goals.append(LTG(ltg_data))
        print("HERE: ", one_user.long_term_goals)
        return one_user


    #? Validations and password hashing for user
    @staticmethod
    def validate_user(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 2:
            flash('First name must have at least 2 characters')
            is_valid = False
        if len(data['last_name']) < 2:
            flash('Last name must have at least 2 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Email must be in proper format')
            is_valid = False
        if User.get_user_by_email(data['email'].lower().strip()):
            flash('Email is already in our system, please try again')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Password and confirm password does not match')
            is_valid = False
        if len(data['password']) <= 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        return is_valid


    @staticmethod
    def parse_user_data(data):
        parsed_data = {}
        parsed_data['first_name'] = data['first_name']
        parsed_data['last_name'] = data['last_name']
        parsed_data['username'] = data['username']
        parsed_data['email'] = data['email']
        parsed_data['password'] = bcrypt.generate_password_hash(data['password'].lower())
        return parsed_data
    
    @staticmethod
    def login_user(data):
        this_user = User.get_user_by_username(data['username'])
        if this_user:
            print('Got this user')
            if bcrypt.check_password_hash(this_user.password, data['password'].lower()):
                session['user_id'] = this_user.id
                session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
                return True
            else:
                flash('Your login failed.')
        else:
            flash('Your login failed')
            return False