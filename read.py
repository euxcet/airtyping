import json
total = 0
with open('words.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        word = line.split()
        if(word[1].isalpha()):
            total += int(word[3])
        else:
            print word[1]

    words = []
    for line in lines:
        word = line.split()
        if(word[1].isalpha()):
            words.append((word[1].lower(), int(word[3]) * 1.0 / total))

    f1 = open('dict.txt', 'w')
    json.dump(words, f1)
