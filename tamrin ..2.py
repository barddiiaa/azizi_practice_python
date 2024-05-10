import re

def interpret_statement(statement):
    if 'not' in statement:
        return False
    return True

def evaluate_suspect(suspect, statements):
    true_count = 0
    false_count = 0
    for statement in statements:
        if interpret_statement(statement[suspect]):
            true_count += 1
        else:
            false_count += 1
    return true_count == false_count

def guilty(sus):
    for suspect in sus:
        if evaluate_suspect(suspect, sus.values()):
            print(f'{suspect} is the thief')

sus = {'a': [False, 'b', True],
       'b': ['not d', 'not a', 'not b'],
       'c': [True, 'not b', True],
       'd': ['d', False, 'a']}

guilty(sus)

