import unittest
from datetime import datetime

from my_message.MyVisitor import MyVisitor


def create_visitor() -> MyVisitor:
    return MyVisitor(
        visitor_id="b297f27e-9544-41d3-b3bc-272e0036d910",
        visitor_ip="66.249.83.219",
        visit_time=datetime.utcnow(),
        url="/test-address"
    )


class MyMessageTestCase(unittest.TestCase):

    def test_constructor(self):
        my_visitor = create_visitor()
        self.assertEqual(my_visitor.id, "b297f27e-9544-41d3-b3bc-272e0036d910")
        self.assertEqual(my_visitor.ip, "66.249.83.219")
        self.assertLessEqual(my_visitor.visit_time, datetime.utcnow())
        self.assertEqual(my_visitor.url, "/test-address")


if __name__ == '__main__':
    unittest.main()
