"""Given a list of strings, generate phrases where they can be joined
example:

Input: ["hello over there",
        "you there, hello",
        "code rocks",
        "writing code"]

Output: ["you there, hello over there",
        "writing code rocks"]
"""

def generate_phrases(phrases):
    first_word = {}
    last_word = {}
    answer = []
    for phrase in phrases:
        new = phrase.split()
        # Add first word keys
        if new[0] not in first_word:
            first_word[new[0]] = [phrase]
        else:
            first_word[new[0]].append(phrase)

        # Add last word keys
        new_phrase = ""
        i = 0
        while i < len(new) - 1:
            new_phrase += new[i] + " "
            i += 1
        if new[len(new) - 1] not in last_word:
            last_word[new[len(new) - 1]] = [new_phrase]
        else:
            last_word[new[len(new) - 1]].append(new_phrase)

        # Search for new phrases
        for key, value in first_word.items():
            if key in last_word:
                for i in value:
                    for j in last_word[key]:
                        answer.append(j + i)

    return set(answer)

print(generate_phrases(["writing code", "code rocks", "code is cool", "what is code"]))
