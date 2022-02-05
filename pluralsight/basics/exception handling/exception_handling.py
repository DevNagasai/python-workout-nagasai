''' A moduel for demonstratin exceptions'''

import typing


def convert(s):
    '''converts to an integer'''
    try:
        x = int(s)
    except ValueError:
        print("conversion failed!")
        x = -1
    except TypeError:
        print("Type error")
    return x


# programmer errors => 
# Indentation error
# syntax error
# Name error

def convert_p(s):
    '''convert to an integer'''
    try:
        x = int(s)
    except(ValueError, TypeError):
        pass # to make the program syntactically correct.
    return x

# to get the name of the error type modify the except statement as follows: 

def convert_know_error_type(s):
    '''converts integer, if wrong prints the error type'''
    try:
        return int(s)
    except Exception as e: 
        return -1 
