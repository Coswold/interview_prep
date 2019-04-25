"""First implementation with O(n) time complexity"""
def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        start = None
        # find the beginning letter
        i = 0
        while i < len(str2):
            if str2[i] == str1[0]:
                start = i
                break
            i += 1
        if start == None:
            return False
        i = 0
        while i < len(str1):
            if start == len(str2):
                start = 0
            if str1[i] != str2[start]:
                return False
            i += 1
            start += 1
        return True

if __name__ == '__main__':
    import sys
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if len(str1) > 0 and len(str2) > 0:
        print(is_rotation(str1, str2))
