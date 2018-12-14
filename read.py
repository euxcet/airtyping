import json
total = 0
with open('en_full.txt', 'r') as f:
    lines = f.readlines()
    for line in lines[0:20000]:
        word = line.split()
        if(word[0].isalpha()):
            total += int(word[1])
        '''
        else:
            print word[1]
        '''

    words = []
    for line in lines[0:20000]:
        word = line.split()
        if(word[0].isalpha()):
            words.append((word[0].lower(), int(word[1]) * 1.0 / total))

    f1 = open('dict.txt', 'w')
    json.dump(words, f1)
