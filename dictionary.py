import json
class Dictionary():
    def __init__(self, path):
        self.entries = []
        with open(path, 'r') as f:
            words = json.load(f)
        # list of [content, prob]
        self.entries = words
