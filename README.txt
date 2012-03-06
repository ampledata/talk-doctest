MMOODDUULLEE  NNAAMMEE
    eat

DDEESSCCRRIIPPTTIIOONN
    DOCTESTS ARE AWESOME!!!!11one

    Exploring the magic and wonder of Python's built-in docstring-based 
    testing mechanism.

    More Info
    =========
        - u' source code for this 
          talk'<http://github.com/ampledata/talk-doctest>
        - u' doctest - Test interactive Python 
          examples'<http://bit.ly/y4WooQ>

    BSP
    ===
        - u' @ampledata on twitter'<http://twitter.com/ampledata>
        - u' ampledata on github'<http://github.com/ampledata>
        - u' ampledata on facebook'<http://facebook.com/ampledata>


FFUUNNCCTTIIOONNSS
    
    eeaatt(food, price=1)
        Eats food, if we have enough cash on hand.
        
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
        RReettuurrnnss::
            A message describing our meal.
        RReettuurrnn  ttyyppee::
            str

VVAARRIIAABBLLEESS
    
    ____ppaacckkaaggee____ = None

