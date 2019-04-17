"""TC: O(n) SC: O(n)"""
def url_ify(string):
    i = 0
    answer = ""
    while i < len(string) - 1:
        if string[i] == ' ' and i - 1 != 0 and string[i + 1].isalpha():
            answer += '%20'
        elif string[i] == ' ':
            i += 1
        else:
            answer += string[i]
        i += 1
    return answer

if __name__ == '__main__':
    import sys
    string = sys.argv[1]  # Ignore script file name
    if len(string) > 0:
        print(url_ify(string))
