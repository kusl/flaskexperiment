import shared
from flask import Flask
from flask_bcrypt import Bcrypt

def get_random_string(length):
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_random_user():
    import uuid
    my_user = add(uuid.uuid4(), get_random_string(8) + "@" + get_random_string(5) + "." + get_random_string(3), get_random_string(8), get_random_string(6) + " " + get_random_string(4))
    return my_user

def add(id, email, password, fullLegalName): 
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    my_user = MyUser(
        id = id,
        email = email,
        password = bcrypt.generate_password_hash(password).decode('utf - 8'),
        fullLegalName = fullLegalName
    )
    return my_user


class MyUser(shared.db.Model): 
    id = shared.db.Column(shared.db.String(40), primary_key=True)
    email = shared.db.Column(shared.db.String(255), nullable=False)
    password = shared.db.Column(shared.db.String(255), nullable=False)
    fullLegalName = shared.db.Column(shared.db.UnicodeText, nullable=False)

    def __init__(
            self,
            id,
            email,
            password,
            fullLegalName
            ):
        self.id = id
        self.email = email
        self.password = password
        self.fullLegalName = fullLegalName

    def __repr__(self):
        return '<MyUser %r>' % self.id

    def __call__(self):
        return {
            "email": self.email,
            "full legal name": self.fullLegalName
        }

    @property
    def serialize(self):
        return {
            "email": self.email,
            "full legal name": self.fullLegalName
        }

    def save(self):
        shared.db.session.add(self)
        shared.db.session.commit()
