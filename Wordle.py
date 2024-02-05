import random
import sys

def main():
    word = getRandomWord()
    oops = 0
    while oops < 6:
        answer = input("Enter a 5 letter guess?")
        for letters in answer:
            if len(answer) > 5 or len(answer) < 5:
                print('Only 5 letter guesses are valid.')
                break
        print()
        printGuessColors(answer, word)
        oops += 1
        if word == answer:
            print(f"You Won! That took {oops} guess(es).")
            break
    if answer != word:
        print(f"You lost. The answer was {word}.")
    
def printGuessColors(answer,word):
    for i in range(5):
        print (letterColor(i,answer,word))
    return


def letterColor(i, answer, word):
    if answer[i] == word[i]:
        return f"{word[i]} - Green"
    elif answer[i] not in word[0:]:
        return f"{answer[i]} - Red"
    else:
        return f"{answer[i]} - Yellow"



def getRandomWord():
   
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
