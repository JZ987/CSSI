#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.

def RemovePunctuation(text):
    punctuations = [",", ".", "?", "/", "<", ">", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}"
                   "~", "`", "'", '"', ":", ";", "-", "_", "+", "="]
    for punctuation in punctuations:
        text = text.replace(punctuation, " ")
    return text

def GetUniqueWordsWithoutPunc(text):
    text = RemovePunctuation(text)
    # unique_words = set(text.lower().split())
    # return len(unique_words)
    dictionary = {}
    text = text.lower().split()
    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print "\nActual unique words: {}".format(len(dictionary))
    print "The top 10 most occuring words are {}".format(GetMostOccuring(dictionary))
    print "The least 10 most occuring words are {}".format(GetLeastOccuring(dictionary))
    print "The number of words appearing 100 and more is {}".format(Count100(dictionary))
    print "The word 'Alice' appeared {} times.".format(dictionary["alice"])
    print "The word 'Wonderland' appeared {} times.\n".format(dictionary["wonderland"])


def GetUniqueWords(text):
    dictionary = {}
    text = text.split()
    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print "\nUnique words: {}".format(len(dictionary))
    print "The top 10 most occuring words are {}".format(GetMostOccuring(dictionary))
    print "The least 10 most occuring words are {}".format(GetLeastOccuring(dictionary))
    print "The number of words appearing 100 and more is {}".format(Count100(dictionary))
    print "The word 'Alice' appeared {} times.".format(dictionary["Alice"])
    print "The word 'Wonderland' appeared {} times.\n".format(dictionary["Wonderland"])

def GetMostOccuring(dictionary):
    return sorted(dictionary, key=dictionary.get, reverse=True)[:10]

def GetLeastOccuring(dictionary):
    return sorted(dictionary, key=dictionary.get)[:10]

def Count100(dictionary):
    count = 0
    for word in dictionary:
        if dictionary[word] >= 100:
            count += 1
    return count

def main():
  # Open the file, read it into memory as a single string.
  with open('Alice.txt') as alice_file:
    alice_text = alice_file.read()

  GetUniqueWords(alice_text)
  GetUniqueWordsWithoutPunc(alice_text)


if __name__ == '__main__':
  main()
