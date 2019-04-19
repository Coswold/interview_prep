def pal_perm(string):
    counts = {}
    length = 0
    # Create Dictionary
    for let in string:
        if let not in counts and let != ' ':
            counts[let] = 1
            length += 1
        elif let != ' ':
            counts[let] += 1
            length += 1
    # Create Threshold
    if length % 2 != 0:
        threshold = 2
    else:
        threshold = 1
    # Search for Palindrome    
    for key, value in counts.items():
        if value % 2 != 0:
            threshold -= 1
        if threshold < 1:
            return False
    return True

if __name__ == '__main__':
    import sys
    string = sys.argv[1]  # Ignore script file name
    if len(string) > 0:
        print(pal_perm(string))
