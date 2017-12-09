import unittest
import uuid
from datetime import datetime

from my_message.MyMessage import MyMessage


class MyMessageTestCase(unittest.TestCase):

    @staticmethod
    def test_constructor():
        message = MyMessage(message_id=uuid.uuid4(), subject="hello, world", sender="hikingfan@gmail.com",
                            sent=datetime.utcnow(), receiver="kushaldeveloper@gmail.com", received=datetime.utcnow(),
                            body="this is an email")
        assert message.body == "this is an email"
        assert message.subject == "hello, world"
        assert message.sender == "hikingfan@gmail.com"
        assert message.receiver == "kushaldeveloper@gmail.com"


if __name__ == '__main__':
    unittest.main()
