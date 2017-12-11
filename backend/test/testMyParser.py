import unittest

from my_message import MyParser


class TfIdfTestCase(unittest.TestCase):

    def setUp(self):
        document = f"<html><br><head>in life i was your partner jacob marley.girl in a mourning-were tears><body><br>"
        self.document = document

    def tearDown(self):
        self.document = None

    def test_score_under_one(self):
        s = MyParser.MyParser()
        s.feed(self.document)
        result = s.get_data()
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
