MODULE NAME
    eat

DESCRIPTION
    DOCTESTS ARE AWESOME!!!!11one
    
    Exploring the magic and wonder of Python's built-in docstring-based testing
    mechanism.
    
    
    Last night a doctest saved my life
    ==================================
      - Builds-in regression testing.
      - Verifies that examples are up-to-date.
      - Creates executable documentation.
    
    
    Running this example
    ====================
      1. Checkout the code from U{ github }
        <http://github.com/ampledata/talk-doctest>}
      2. From a command prompt: C{ $ python eat.py }
        - This should produce NO output.
        - To actually see what happened,
          add the C{ -v } flag: C{ $ python eat.py -v }
    
            Trying:
                lunch='taco'
            Expecting nothing
            ok
    
    
    More Info
    =========
      - U{ source code for this talk <http://github.com/ampledata/talk-doctest>}
      - U{ doctest - Test interactive Python examples <http://bit.ly/y4WooQ>}
    
    
    BSP
    ===
      - U{ @ampledata on twitter <http://twitter.com/ampledata>}
      - U{ ampledata on github <http://github.com/ampledata>}
      - U{ ampledata on facebook <http://facebook.com/ampledata>}

FUNCTIONS
    
    eat(food, price=1)
        Eats food, if we have enough cash on hand.
        
        Test & Example
        ==============
            - Eating a regulation taco:
                >>> lunch='taco'
                >>> eat(lunch)
                'Eating a delicious taco for $1.' #+doctest.NORMALIZE_WHITESPACE
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

