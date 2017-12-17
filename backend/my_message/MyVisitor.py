import shared


def save_visitor(this_request) -> bool:
    import uuid
    from datetime import datetime
    visitor = MyVisitor(visitor_id=uuid.uuid4(),
                        visitor_ip=this_request.remote_addr,
                        visit_time=datetime.now(),
                        url=f"{this_request.full_path}")
    visitor.save()
    return True


class MyVisitor(shared.db.Model):
    id = shared.db.Column(shared.db.String(40), primary_key=True)
    ip = shared.db.Column(shared.db.UnicodeText, nullable=False)
    visit_time = shared.db.Column(shared.db.DateTime, nullable=False)
    url = shared.db.Column(shared.db.UnicodeText, nullable=False)

    def __init__(
            self,
            visitor_id,
            visitor_ip,
            visit_time,
            url):
        self.id = visitor_id
        self.ip = visitor_ip
        self.visit_time = visit_time
        self.url = url

    def __repr__(self):
        return '<MyVisitor %r>' % self.id

    def __call__(self):
        return {
            "id": self.id,
            "ip": self.ip,
            "time": self.visit_time}

    @property
    def serialize(self):
        return {
            "ip": self.ip,
            "time": self.visit_time
        }

    def save(self):
        shared.db.session.add(self)
        shared.db.session.commit()
