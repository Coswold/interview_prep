'''You are given two strings - where the first string can include regex wildcard characters (* and ?)
and other is a regular string.
Write a method to check if the two strings match.

* --> Matches with zero or more characters.

? --> Matches exactly a single character.'''

def match(first, second):
    while len(first) > 0:
        if len(second) < 1:
            return False

        if first[0] == second[0] or first[0] == '?':
            first = first[1:]
            second = second[1:]
        elif first[0] == '*':
            while first[0] == '*':
                first = first[1:]
            while first[0] != second[0]:
                second = second[1:]
        else:
            return False

    if len(second) > 0 or len(first) > 0:
        return False
    else:
        return True
