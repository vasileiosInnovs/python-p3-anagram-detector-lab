# your code goes here!

words = ['google', 'inlets', 'banana']

class Anagram:
    def __init__(self, target):
        self.target = target

    def match(self, word_list):
        return [word for word in word_list if sorted(word) == sorted(self.target)]
            
listen = Anagram("listen")
print(listen.match(words))