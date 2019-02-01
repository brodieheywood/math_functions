from unittest import TestCase
from math_functions import q04


class TestDijkstra(TestCase):
    def test_dijkstra_one(self):
        dutch = ['white']
        flag = ['white']
        q04.dijkstra(dutch)
        self.assertEqual(dutch, flag)

    def test_dijkstra_smallest_case(self):
        dutch = ['white', 'blue']
        flag = ['white', 'blue']
        q04.dijkstra(dutch)
        self.assertEqual(dutch, flag)

    def test_dijkstra_general_case(self):
        dutch = ['white', 'blue', 'white']
        flag = ['white', 'white', 'blue']
        q04.dijkstra(dutch)
        self.assertEqual(dutch, flag)

    def test_dijkstra_not_flag_colours(self):
        dutch = ['white', 'blue', 'white']
        flag = ['brown', 'white', 'blue']
        q04.dijkstra(dutch)
        self.assertNotEqual(dutch, flag)

    def test_dijkstra_larger_case(self):
        dutch = ['white', 'blue', 'blue', 'white', 'blue', 'blue', 'red', 'white', 'red', 'white', 'blue', 'blue']
        flag = ['red', 'red', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
        q04.dijkstra(dutch)
        self.assertEqual(dutch, flag)
