import unittest

from io_group import IOGroup
from single_io import BooleanIO


class TestGroup(IOGroup):
    Bool1 = BooleanIO("Boolean 1", "Bool1", False)


class TestReadWrite(unittest.TestCase):

    def setUp(self):
        self.group = TestGroup()

    def test_that_dumps_produces_appropriate_result(self):
        print(self.group.dumps())
