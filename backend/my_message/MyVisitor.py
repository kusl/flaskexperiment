import shared
from sqlalchemy.dialects.postgresql.json import JSONB

class MyVisitor(shared.db.Model):
    id = shared.db.Column(shared.db.String(40), primary_key=True)
    ip = shared.db.Column(shared.db.UnicodeText, nullable=False)
    visit_time = shared.db.Column(shared.db.DateTime, nullable=False)
    visitor_info = shared.db.Column(JSONB)

    def __init__(
            self,
            visitor_id,
            visitor_ip,
            visit_time,
            visitor_info):
        self.id = visitor_id
        self.visit_time = visit_time
        self.visitor_info = visitor_info

    def __repr__(self):
        return '<MyVisitor %r>' % self.id

    def __call__(self):
        return {
            "id": self.id,
            "ip": self.visitor_ip,
            "time": self.visit_time}

    @property
    def serialize(self):
        return {
            "id": self.id,
            "ip": self.ip
        }

    def save(self):
        shared.db.session.add(self)
        shared.db.session.commit()

