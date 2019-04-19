def search_and_replace(str1, str2):
    i = 0
    count = 0
    # Check differences by character
    while i < len(str1):
        if str1[i] != str2[i]:
            count += 1
        if count > 1:
            return False
        i += 1
    return True

def search_and_remove(str1, str2):
    i = 0
    j = 0
    count = 0
    # Check differences by character
    while i < len(str2):
        if str1[i] != str2[j]:
            count += 1
            i += 1
            if count > 1:
                return False
        else:
            i += 1
            j += 1
    return True

def one_away(str1, str2):
    if len(str1) == len(str2):
        return search_and_replace(str1, str2)
    elif len(str1) == len(str2) + 1:
        return search_and_remove(str1, str2)
    elif len(str1) + 1 == len(str2):
        return search_and_remove(str2, str1)
    return False


if __name__ == '__main__':
    import sys
    str1 = sys.argv[1]  # Ignore script file name
    str2 = sys.argv[2]
    if len(str1) > 0 or len(str2) > 0:
        print(one_away(str1, str2))
