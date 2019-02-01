# Brodie Heywood
# November 26, 2018

"""Dijkstra's DNF Problem"""

import doctest


def dijkstra(dutch):
    """Solve Dutch National Flag problem.

    Rearrange colour names into the order of the Dutch flag: red, white, then blue.
    PARAM: dutch, list of randomly ordered strings: 'red', 'white', and 'blue'
    PRECONDITION: dutch parameter must be a non-empty list that contains strings 'red', 'white', and 'blue'
    POSTCONDITION: lists strings 'red', 'white', and 'blue' in the order of the Dutch flag
    RETURN: none
    >>> dijkstra(['white', 'blue', 'blue', 'red', 'white', 'red', 'white'])
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
    >>> dijkstra(['white', 'blue', 'red'])
    ['red', 'white', 'blue']
    >>> dijkstra(['blue'])
    ['blue']
    >>> dijkstra(['blue', 'blue'])
    ['blue', 'blue']
    """
    dutch.sort(key=sorting_out_the_dutch)
    return dutch


def sorting_out_the_dutch(dutch_list):
    return dutch_list[2]


def main():
    dutch = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
    dijkstra(dutch)
    print(dutch)


if __name__ == '__main__':
    main()
    doctest.testmod()
