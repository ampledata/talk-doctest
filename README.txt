MODULE NAME
    eat

DESCRIPTION
    DOCTESTS ARE AWESOME!!!!11one

    Exploring the magic and wonder of Python's built-in docstring-based 
    testing mechanism.

    Last night a doctest saved my life
    ==================================
        - Build-in regression testing.
        - Verify that examples are up-to-date.
        - Create executable documentation.
        - Create in-line Examples.
        - Leave the campground cleaner than you found it.

    Running this example
    ====================
        1. Checkout the code from u' 
           github'<http://github.com/ampledata/talk-doctest>
        2. From a command prompt:  $ python eat.py
             - This should produce NO output.
             - To actually see what happened, add the  -v  flag:  $ python 
               eat.py -v

    More Info
    =========
        - u' source code for this 
          talk'<http://github.com/ampledata/talk-doctest>
        - u' doctest - Test interactive Python 
          examples'<http://bit.ly/y4WooQ>
        - u' Epydoc - Automatic API Documenation Generator for 
          Python'<http://epydoc.sourceforge.net/>

    BSP
    ===
        - u' @ampledata on twitter'<http://twitter.com/ampledata>
        - u' ampledata on github'<http://github.com/ampledata>
        - u' ampledata on facebook'<http://facebook.com/ampledata>


FUNCTIONS
    
    eat(food, price=1)
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
        Returns:
            A message describing our meal.
        Return type:
            str

VARIABLES
    
    __package__ = None

