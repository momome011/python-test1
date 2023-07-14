import random
def scramble(sentence):
    words = []
    for word in  sentence.split():
        if len(word) > 1:
            words.append(word[0]
                       + ''.join(random.sample([char for char in word[1:-1]], len(word) - 2))+ word[-1])
        else:
            words.append(word)
    return ' '.join(words)
text= '''Shuffle words in this sentence.
 Python has a limitless number of packages used in everyday programming. 
 当数组边界超过最大限定，将会抛出异常
'''
new = scramble(text)
print(new)
