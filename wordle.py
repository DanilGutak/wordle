def search_letter(word, letter, i, answer):
    count = 0
    j = 0
    start_index = 0

    while(j in range(len(word))):
        j = 0
        j = word.find(letter, start_index)
        if(j == i):
            answer[i] = 'g'
        elif(j >= 0 and count == 0):
            answer[i] = 'y'
        if (j != -1):
            start_index = j+1
            count += 1

def check_guess(guess):
    f = open("words.txt", "r")
    s = f.read()
    j = s.find(guess, 0)
    if (j == -1):
        return(-1)

def choose_word():
    import random
    f = open("words.txt", "r")
    s = f.read()
    words = list(map(str, s.split('\n')))
    word_pos = random.randint(0, len(words)-1)
    word = words[word_pos]
    print(word)
    return(word)

def check_letters(word, input_text, j):
    guess = input_text
    answer = list("00000")
    i = 0
    print(word)
    while(i < 5):
        search_letter(word, guess[i], i, answer)
        i+=1
    print (answer)
    j+=1
    if(j == 6):
        j = 0
    return(j)

if __name__ == "__main__":
    main()