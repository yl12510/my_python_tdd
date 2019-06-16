# -*- coding: utf-8 -*-

import unittest

from mycode import hello_world


class MyTest(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
