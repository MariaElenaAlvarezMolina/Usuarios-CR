from mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, email) VALUES( %(first_name)s, %(last_name)s, %(email)s )"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        users = []
        for u in results:
            user = cls(u)
            users.append(user)
        return users