import json
import unittest
import uuid
from datetime import datetime

from my_message.MyMessage import MyMessage
from my_message.MyMessage import create_random_message


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

    def test_load_from_json(self):
        data = json.load(open("sample/example.json"))
        for element in data:
            print(element)
        self.assertIsNotNone(data)

    def test_create_random_message(self):
        message = create_random_message()
        self.assertIsNotNone(message.id)
        self.assertIsNotNone(message.subject)
        self.assertIsNotNone(message.sender)
        self.assertIsNotNone(message.sent)
        self.assertIsNotNone(message.receiver)
        self.assertIsNotNone(message.received)
        self.assertIsNotNone(message.body)


if __name__ == '__main__':
    unittest.main()
