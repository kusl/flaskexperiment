import uuid
from datetime import datetime

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


def create_message():
    print(uuid.uuid4())
    my_message = MyMessage(
        message_id=uuid.uuid4(),
        sender="spamkushal@gmail.com",
        sent=datetime.utcnow(),
        receiver="kushalpublic@gmail.com",
        received=datetime.utcnow(),
        subject="Three weird tricks to make money, number five will shock you!",
        body=f"This Bluetooth speaker has a feature that sets it apart from the crowd. "
             f"It’s got an ejectable, rechargeable battery you can use as a powerbank, "
             f"which is cool, but that’s not exactly the feature we’re talking about. "
             f"It’s this: When you hit the eject button for the battery, "
             f"it comes out smoothly and extremely satisfyingly.")
    shared.db.session.add(my_message)
    shared.db.session.commit()


@app.route('/clear', methods=['GET'])
def drop_and_create():
    shared.db.drop_all()
    shared.db.create_all()
    return 'Create All ' + str(datetime.utcnow())


if __name__ == '__main__':
    app.run()
