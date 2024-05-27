"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    favorite_vegetable = input("what is your favorite vegetable?")
    first = "Interesting! I also love "
    last = "!"
    print(first, favorite_vegetable, last, sep="")


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    favorite_number = input("what is your favorite number?")
    first = "Interesting! I also love "
    last = "!"
    print(first, favorite_number, last, sep="")


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name = input("what is your name?")
    sign = input("what is your zodiac sign?")
    first = "Interesting! My name is also "
    second = ", and I'm also a "
    last = "!"
    print(first, name, second, sign, last, sep="")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name = input("what is your name?")
    age = input("what is your age?")
    first = "Interesting! My name is also "
    second = ", and I'm also "
    last = " years old!"
    print(first, name, second, age, last, sep="")
