#!/usr/bin/env python
"""DOCTESTS ARE AWESOME!!!!11one

More Info
=========
  - U{doctest - Test interactive Python examples<http://bit.ly/y4WooQ>}
"""

__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Public Domain.'
__license__ = 'Steal this example.'


import doctest
import argparse

#class RunDoctests(argparse.Action, doctest
#class FooAction(argparse.Action):
#        def __call__(self, parser, namespace, values, option_string=None):
#                    print '%r %r %r' % (namespace, values, option_string)
#                            setattr(namespace, self.dest, values)


def eat(food, price=1):
    """Eats food, if we have enough cash on hand.

    Test & Example
    ==============
        - Eating a regulation taco:

            >>> lunch='taco'
            >>> eat(lunch)
            'Eating a delicious taco for $1.'

        - Eating an engineer's food pellet for $3:

            >>> dinner='burrito'
            >>> eat(dinner, 3)
            'Eating a delicious burrito for $3.'

        - Indecisiveness is a killer:

            >>> eat()
            Traceback (most recent call last):
            TypeError: eat() takes at least 1 argument (0 given)

        - After the lay-off:

            >>> eat('sandwich', 6)
            "I can't afford that!"


    Operation
    =========
        @param food: Something to eat.
        @param price: Price of our meal.
        @type food: str
        @type price: int

        @rtype: str
        @return: A message describing our meal.
    """
    cash_on_hand = 5
    if price <= cash_on_hand:
        meal = 'Eating a delicious %s for $%s.' % (food, price)
    else:
        meal = "I can't afford that!"
    return meal


# There's several ways to invoke the doctest within eat():
#
# 1. Call doctest.testmod() as our main.

if __name__ == '__main__':
    doctest.testmod()


# 2. Create a test function, itself calling doctest.testmod().
#     - Helpful if we want to use opt^H^H^Hargparse to invoke tests.
#     - Akin to Tim Peters' original example: http://bit.ly/ziUfgu

def test_eat():
    """Runs the doctests within the L{eat()} function."""
    doctest.testmod()

if __name__ == '__main__':
    # something something argparse
    # if opt='test'
    test_eat()
    # else:
    # normal_stuff()


# 3. Use py.test to execute our doctest.
#   - Helpful for libraries where a __main__ may not exist.
#   - See also: http://pytest.org/latest/doctest.html
#
# $ py.test --doctest-modules
