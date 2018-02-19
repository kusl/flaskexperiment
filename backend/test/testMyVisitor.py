import unittest
from datetime import datetime

from my_message.MyVisitor import MyVisitor


def create_visitor() -> MyVisitor:
    return MyVisitor(
        visitor_id="b297f27e-9544-41d3-b3bc-272e0036d910",
        visitor_ip="66.249.83.219",
        visit_time=datetime.utcnow(),
        url="/test-address",
        user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
    )


class MyVisitorTestCase(unittest.TestCase):

    def test_constructor(self):
        my_visitor = create_visitor()
        self.assertEqual(my_visitor.id, "b297f27e-9544-41d3-b3bc-272e0036d910")
        self.assertEqual(my_visitor.ip, "66.249.83.219")
        self.assertLessEqual(my_visitor.visit_time, datetime.utcnow())
        print(my_visitor.url)
        self.assertEqual(my_visitor.url, "/test-address")
        self.assertEqual(my_visitor.user_agent, "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0")


if __name__ == '__main__':
    unittest.main()
