"""First implementation was broken"""
def string_compress_faulty(string):
    counts = {}
    compression = ""
    for let in string:
        if let not in counts:
            counts[let] = 1
        else:
            counts[let] += 1
    for key, value in counts.items():
        compression += (key + str(value))
    if len(compression) < len(string):
        return compression
    else:
        return string

"""Second Implementation"""
def string_compress(string):
    compression = ""
    i = 0
    while i < len(string):
        count = 1
        while i < len(string) - 1 and string[i] == string[i + 1]:
            count += 1
            i += 1
        compression += (string[i] + str(count))
        i += 1
    if len(compression) <= len(string):
        return compression
    else:
        return string

if __name__ == '__main__':
    import sys
    string = sys.argv[1]  # Ignore script file name
    if len(string) > 0:
        print(string_compress(string))
