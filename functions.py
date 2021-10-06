# def greeting():
#     print('hello Rob')

# # prints nothing

# ====================================================================================================

# def greeting(name):
#     print('Hello', name)


# greeting('Erin')
# greeting('Paolo')
# greeting('Tanya')

# # Hello Erin
# # Hello Paolo
# # Hello Tanya

# ====================================================================================================


# def about_me(fave_food, fave_animal, fave_place):
#     print('I love to eat', fave_food, 'while petting my',
#           fave_animal, 'at', fave_place)


# # about_me('sushi', 'cat', 'the beach')
# # I love to eat sushi while petting my cat at the beach

# ====================================================================================================

# about_me("the beach", "sushi", "cat")

# # I love to eat sushi while petting my cat at the beach

# ====================================================================================================

# about_me(fave_place="the beach", fave_food="sushi", fave_animal="cat")

# # I love to eat sushi while petting my cat at the beach

# ====================================================================================================

# def accept_phone(number, phone_type):
#     print('The phone number', number, 'is a', phone_type, 'phone')


# accept_phone('555-1234', 'home')
# accept_phone('555-5678', 'cell')
# accept_phone('555-8765', 'work')

# # The phone number 555-1234 is a home phone
# # The phone number 555-5678 is a cell phone
# # The phone number 555-8765 is a work phone

# ====================================================================================================

# def accept_phone(number, phone_type="cell"):
#     print('The phone number', number, 'is a', phone_type, 'phone')


# accept_phone('555-1234', 'home')
# accept_phone('555-5678', 'cell')
# accept_phone('555-8765', 'work')
# accept_phone('555-1122')

# # The phone number 555-1234 is a home phone
# # The phone number 555-5678 is a cell phone
# # The phone number 555-8765 is a work phone
# # The phone number 555-1122 is a cell phone

# ====================================================================================================

# def greeting():
#     print('hello', name)


# name = 'marco'
# greeting()

# # hello marco

# ====================================================================================================

# def greeting():
#     name = 'Maria'
#     print('Hello', name)


# name = 'Marco'
# greeting()

# # Hello Maria

# ====================================================================================================

# def greeting():
#     print('Hello', name)
#     name = 'Maria'
#     print('Hello', name)


# name = 'Marco'
# greeting()

# # Traceback (most recent call last):
# #   File "/Users/robertestrella/Desktop/SEI802/Unit-4/labs/intro_to_python/functions.py", line 106, in <module>
# #     greeting()
# #   File "/Users/robertestrella/Desktop/SEI802/Unit-4/labs/intro_to_python/functions.py", line 100, in greeting
# #     print('Hello', name)
# # UnboundLocalError: local variable 'name' referenced before assignment

# ====================================================================================================

# def greeting():
#     global name
#     print('Hello', name)
#     name = 'Maria'
#     print('Hello', name)


# name = 'Marco'
# greeting()

# # Hello Marco
# # Hello Maria

# ====================================================================================================
