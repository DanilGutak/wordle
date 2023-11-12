import sys

def search_letter(word, answer, guess):
    i = 0
    while(i < 5):
        if(guess[i] == word[i]):
            answer[i] = 'g'
        i+=1
    i = 0
    j = 0
    while(i < 5):
        while(j < 5):
            if(guess[i] == word[j] and answer[i] == '0' and answer[j] != 'g'):
                answer[i] = 'y'
            j+=1
        i+=1
        j = 0
    i = 0
    while(i < 5):
        k = 0
        j = 4
        while(word.count(guess[i]) < (guess.count(guess[i]) - k)):
            while(j >= 0 and (guess[j] != guess[i] or guess[j] == word[j])):
                j-=1
            answer[j] = '0'
            j-=1
            k += 1
        i += 1

def check_guess(guess):
    try:
        with open("words.txt", "r") as f:
            s = f.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    j = s.find(guess, 0)
    if (j == -1):
        return(-1)

def choose_word():
    import random
    try:
        with open("words.txt", "r") as f:
            s = f.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    words = list(map(str, s.split('\n')))
    word_pos = random.randint(0, len(words)-1)
    word = words[word_pos]
    #print(word)
    return(word)