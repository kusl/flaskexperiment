import unittest
import uuid
from datetime import datetime

from my_message.MyMessage import MyMessage


class MyMessageTestCase(unittest.TestCase):

    def test_constructor(self):
        message = MyMessage(
            message_id=uuid.uuid4(),
            subject="hello, world",
            sender="hikingfan@gmail.com",
            sent=datetime.utcnow(),
            receiver="kushaldeveloper@gmail.com",
            received=datetime.utcnow(),
            body="this is an email")
        self.assertEqual(message.body, "this is an email")
        self.assertEqual(message.subject, "hello, world")
        self.assertEqual(message.sender, "hikingfan@gmail.com")
        self.assertEqual(message.receiver, "kushaldeveloper@gmail.com")


if __name__ == '__main__':
    unittest.main()
