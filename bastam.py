from copy import deepcopy


def guilty(sus):

    suspect_list = ['a', 'b', 'c', 'd']

    for guilty in suspect_list:
        list1 = deepcopy(list(sus.values()))

        for statement in list1:
            for i in range(3):
                if statement[i] == guilty:
                    statement[i] = True
                elif 'not ' + guilty == statement[i]:
                    statement[i] = False
                elif type(statement[i]) != bool:
                    if 'not ' in statement[i]:
                        statement[i] = True
                    else:
                        statement[i] = False

        true_count = 0
        false_count = 0

        for statement in list1:
            for i in statement:
                if i == True:
                    true_count += 1
                else:
                    false_count += 1

        if true_count == 6 and false_count == 6:
            print(f'{guilty} is the thief')


sus = {'a': [False, 'b', True],
       'b': ['not d', 'not a', 'not b'],
       'c': [True, 'not b', True],
       'd': ['d', False, 'a']}

guilty(sus)

sus = {'a': [False, 'b', True],
       'b': ['not d', 'not a', 'not b'],
       'c': [True, 'not b', False],
       'd': ['d', True, 'a']}

guilty(sus)

sus = {'a': [True, 'b', True],
       'b': ['not d', 'not a', 'not b'],
       'c': [False, 'not b', True],
       'd': ['d', False, 'a']}

guilty(sus)

sus = {'a': [True, 'b', True],
       'b': ['not d', 'not a', 'not b'],
       'c': [False, 'not b', False],
       'd': ['d', True, 'a']}

guilty(sus)
