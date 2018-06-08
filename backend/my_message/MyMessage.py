import shared


def get_random_string(length):
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def add(sender, receiver, subject, body):
    import uuid
    from datetime import datetime, timedelta
    my_message = MyMessage(
        message_id=uuid.uuid4(),
        sender=sender,
        sent=datetime.utcnow(),
        receiver=receiver,
        received=datetime.utcnow(),
        subject=subject,
        body=body)
    return my_message


def create_random_message():
    import uuid
    from datetime import datetime, timedelta
    my_message = MyMessage(
        message_id=uuid.uuid4(),
        sender=f"{get_random_string(8)}@{get_random_string(5)}.{get_random_string(3)}",
        sent=(datetime.utcnow() - timedelta(minutes=10)).date().isoformat(),
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


def create_random_messages(number_of_messages):
    messages = []
    for n in range(number_of_messages):
        messages.append(create_random_message())
    return messages


def get_message_by_id(input_id):
    return MyMessage.query.filter_by(id=input_id).first()


class MyMessage(shared.db.Model):
    id = shared.db.Column(shared.db.String(40), primary_key=True)
    subject = shared.db.Column(shared.db.UnicodeText, nullable=False)
    sender = shared.db.Column(shared.db.String(255), nullable=False)
    sent = shared.db.Column(shared.db.DateTime, nullable=False)
    receiver = shared.db.Column(shared.db.String(255), nullable=False)
    received = shared.db.Column(shared.db.DateTime, nullable=False)
    body = shared.db.Column(shared.db.UnicodeText, nullable=False)
    score = shared.db.Column(shared.db.Float, nullable=False, default=0.0)

    def __init__(
            self,
            message_id,
            subject,
            sender,
            sent,
            receiver,
            received,
            body):
        self.id = message_id
        self.subject = subject
        self.sender = sender
        self.sent = sent
        self.receiver = receiver
        self.received = received
        self.body = body

    def __repr__(self):
        return '<MyMessage %r>' % self.id

    def __call__(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "subject": self.subject,
            "sent": self.sent,
            "receiver": self.receiver,
            "received": self.received,
            "body": self.body}

    @property
    def serialize(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "sender": self.sender,
            "sent": self.sent,
            "receiver": self.receiver,
            "received": self.received,
            "body": self.body
        }

    def save(self):
        shared.db.session.add(self)
        shared.db.session.commit()
