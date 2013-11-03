import unittest

from robin_map import RobinMap


class TestRobinMap(unittest.TestCase):

    def test_should_get_none_value_from_empty_map(self):
        map = RobinMap()

        value = map.get("key")

        self.assertEquals(None, value)


    def test_should_put_and_get_value(self):
        map = RobinMap()
        map.put("num", 0)

        self.assertEquals(0, map.get("num"))


    def test_should_put_value_when_key_not_in_map(self):
        map = RobinMap()

        map.put("num", 0)

        self.assertEquals(0, map.get("num"))


    def test_should_not_put_new_value_when_key_already_in_map(self):
        map = RobinMap()
        map.put("num", 0)

        map.put("num", 1)

        self.assertEquals(1, map.get("num"))








    def test_should_do_nothing_when_removing_value_from_empty_map(self):
        map = RobinMap()

        value = map.remove("key")

        self.assertEquals(None, value)


    def test_should_remove_value_when_key_exists_in_map(self):
        map = RobinMap()
        map.put("num", 0)

        map.remove("num")

        self.assertEquals(0, len(map))