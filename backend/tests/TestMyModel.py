import unittest
import uuid
from datetime import datetime

import models.MyMessage as M


class TestMyModel(unittest.TestCase):

    def test_upper(self):
        message = M(message_id=uuid.uuid4(),
                    subject="hello, world",
                    sender="hikingfan@gmail.com",
                    sent=datetime.utcnow(),
                    receiver="kushaldeveloper@gmail.com",
                    received=datetime.utcnow(),
                    body="this is an email")
        assert message.body == "this is an email"


if __name__ == '__main__':
    unittest.main()
