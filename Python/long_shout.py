VOWELS = ["A", "E", "I", "O", "U"]
word = "hello"

def LongShout(word):
    word = word.upper()
    for vowel in VOWELS:
        word = word.replace(vowel, vowel * 5)
    return word

print LongShout(word)
