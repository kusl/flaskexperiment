import json
import string
import uuid
from datetime import datetime

import random
from flask import Blueprint
from flask import jsonify

import shared
from my_message.MyMessage import MyMessage

MyMessageRoute = Blueprint('my_message_route', __name__)


@MyMessageRoute.route('/api/v0/my_message/first')
def get_first_message():
    return jsonify(MyMessage.query.first().serialize)


@MyMessageRoute.route('/api/v0/my_message/all')
def get_all_messages():
    return json.dumps(MyMessage.query.all().serialize)


@MyMessageRoute.route('/api/v0/my_message/add')
def hello_world():
    result = create_message()
    shared.db.session.add(result)
    shared.db.session.commit()
    return "done"


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_message():
    my_message = MyMessage(
        message_id=uuid.uuid4(),
        sender=f"{get_random_string(8)}@{get_random_string(5)}.{get_random_string(3)}",
        sent=datetime.utcnow(),
        receiver=f"{get_random_string(8)}@{get_random_string(5)}.{get_random_string(3)}",
        received=datetime.utcnow(),
        subject=f"{get_random_string(5)} {get_random_string(8)} {get_random_string(3)}",
        body=f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. "
             f"{get_random_string(5)} {get_random_string(8)} {get_random_string(6)} {get_random_string(3)}. ")
    return my_message
