import string
import uuid
from datetime import datetime

import random
from flask import Flask

import secret
import shared
from models.MyMessage import MyMessage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(app)


@app.route('/')
def hello_world():
    create_message()
    return 'Hello World!'


def return_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_message():
    my_message = MyMessage(
        message_id=uuid.uuid4(),
        sender=f"{return_random_string(8)}@{return_random_string(5)}.{return_random_string(3)}",
        sent=datetime.utcnow(),
        receiver=f"{return_random_string(8)}@{return_random_string(5)}.{return_random_string(3)}",
        received=datetime.utcnow(),
        subject=f"{return_random_string(5)} {return_random_string(8)} {return_random_string(3)}",
        body=f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. "
             f"{return_random_string(5)} {return_random_string(8)} {return_random_string(6)} {return_random_string(3)}. ")
    shared.db.session.add(my_message)
    shared.db.session.commit()


@app.route('/clear', methods=['GET'])
def drop_and_create():
    shared.db.drop_all()
    shared.db.create_all()
    return 'Create All ' + str(datetime.utcnow())


if __name__ == '__main__':
    app.run()
