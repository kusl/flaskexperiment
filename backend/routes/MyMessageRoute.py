import string
import uuid
from datetime import datetime

import random
from flask import Blueprint, jsonify, render_template

from my_message.MyMessage import MyMessage

MyMessageRoute = Blueprint('my_message_route', __name__)


@MyMessageRoute.route('/api/v0/my_message/first')
def get_first_message():
    result = MyMessage.query.first()
    if result is None:
        return jsonify({"error": "There is no message"})
    return jsonify(result.serialize)


@MyMessageRoute.route('/api/v0/my_message/add')
def hello_world():
    create_message().save()
    return render_template("pages/add.html")


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
