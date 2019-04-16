""" This is a O(n) time complexity solution and O(n) space complexity """
def is_unique(string):
    checked = {}
    for let in string:
        if let not in checked:
            checked[let] = 1
        else:
            return False
    return True

""" This is a O(n^2) time complexity solution and O(1) space complexity.
    Implemented with no extra data structures. """
def is_unique2(string):
    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string):
            if string[i] == string[j]:
                return False
            j += 1
        i += 1
    return True


if __name__ == '__main__':
    import sys
    string = sys.argv[1]  # Ignore script file name
    if len(string) > 0:
        print(is_unique(string))
        print(is_unique2(string))
