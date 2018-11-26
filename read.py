import json
total = 0
with open('words.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        word = line.split()
        total += int(word[3])

    words = []
    for line in lines:
        word = line.split()
        words.append((word[1], int(word[3]) * 1.0 / total))

    f1 = open('dict.txt', 'w')
    json.dump(words, f1)
