import random

words = ['braian','java','corazon']
word = random.choice(words)

hidden_letters= int(len(word) * 0.6)
hidden_positions = random.sample(range(len(word)),hidden_letters)

hidden_word = ""
for index, letter in enumerate(word):
    hidden_word += "_" if index in hidden_positions else letter

    
