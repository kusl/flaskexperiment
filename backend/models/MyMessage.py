from shared import db


class MyMessage(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    subject = db.Column(db.UnicodeText, nullable=False)
    sender = db.Column(db.String(255), nullable=False)
    sent = db.Column(db.DateTime, nullable=False)
    receiver = db.Column(db.String(255), nullable=False)
    received = db.Column(db.DateTime, nullable=False)
    body = db.Column(db.UnicodeText, nullable=False)
    score = db.Column(db.Float, nullable=False, default=0.0)

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

    @property
    def serialize(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "sender": self.sender,
            "sent": self.sent,
            "receiver": self.receiver,
            "body": self.body
        }
