import json
total = 0
maxlength = 0
with open('en_full.txt', 'r') as f:
    lines = f.readlines()
    for line in lines[0:20000]:
        word = line.split()
        if(word[0].isalpha()):
            total += int(word[1])
            maxlength = max(maxlength, len(word[0]))
        '''
        else:
            print word[1]
        '''

    words = [[] for i in xrange(maxlength + 1)]
    for line in lines[0:20000]:
        word = line.split()
        if(word[0].isalpha()):
            words[len(word[0])].append((word[0].lower(), int(word[1]) * 1.0 / total))

    f1 = open('dict_bylength.txt', 'w')
    json.dump(words, f1)
