from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query, {'id':data})

    @classmethod
    def select(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        return connectToMySQL('users_schema').query_db(query, {'id':data})

    @classmethod
    def select_last(cls):
        query = 'select * FROM users ORDER BY id DESC LIMIT 1;'
        return connectToMySQL('users_schema').query_db(query)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query, data)