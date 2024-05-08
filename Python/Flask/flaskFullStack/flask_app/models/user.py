from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db_name = 'userspython2024'
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def createUser(cls, data):
        query = 'INSERT INTO users (username, email, password) VALUES ( %(username)s, %(email)s, %(password)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def getAllUsers(cls):
        query = "SELECT id, username, email FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        if results:
            for eachUser in results:
                users.append(eachUser)
        return users
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users where id = %(id)s;"
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM USERS WHERE id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users set username = %(username)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)