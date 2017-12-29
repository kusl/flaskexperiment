import unittest

from my_message import MyParser


class TfIdfTestCase(unittest.TestCase):

    def setUp(self):
        document = """<br><br><a href="https://s3.amazonaws.com/b2asiandating1/35000.html">View my Pics Now. It's Free!</a><br><br>"""
        self.document = document

    def tearDown(self):
        self.document = None

    def test_sanity_check_my_parser(self):
        s = MyParser.MyParser()
        s.feed(self.document)
        result = s.get_data()
        print(result)
        self.assertIsNotNone(result)
        print(result, "View my Pics Now. It's Free!")


if __name__ == '__main__':
    unittest.main()
