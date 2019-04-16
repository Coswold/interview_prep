"""TC: O(n); SC: O(n)"""
def is_perm(str1, str2):
    # If strings arent the same length, they can't be permutations
    if len(str1) != len(str2):
        return False

    # Create a dictionary to store counts of first string
    count = {}
    for letter in str1:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

    # Check to make sure all letters are in the second string
    for letter in str2:
        if letter not in count:
            return False
        elif count[letter] < 0:
            return False
        else:
            count[letter] -= 1

    return True

if __name__ == '__main__':
    import sys
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if len(str1) > 0 and len(str2) > 0:
        print(is_perm(str1, str2))
