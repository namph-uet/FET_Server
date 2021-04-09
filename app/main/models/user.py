class User(object):
    def __init__(self, email, username, password, registered_on):
        self.email = email
        self.username = username
        self.password = password
        self.registered_on = registered_on
    
    def __str__(self):
        return f"User id: {self.id}"