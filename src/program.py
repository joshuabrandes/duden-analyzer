import duden


# writing analyze() function
def analyze():
    if position == '1':
        wordList = duden.search(word=letter, exact=False)
        print("Words in Duden starting with " + letter + ": " + str(len(wordList)))
    elif position > '1':
        wordList = duden.search(word=letter, exact=False)
        print("Words in Duden starting with " + letter + ": " + str(len(wordList)))
        print("Words in Duden starting with " + letter + " in position " + position + ": " + str(len(wordList)))


# Setup
print('Choose one option: '
      '\n1. Search for a word'
      '\n2. Analyze by letter')
option = input('Option: ')
if option == '1':
    word = input('Word: ')
    print(duden.search(word))
elif option == '2':
    letter = input('Letter: ')
    position = input('Position: ')
    analyze()
