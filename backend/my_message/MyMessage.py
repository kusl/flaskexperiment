import shared


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
