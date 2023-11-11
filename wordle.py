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
            if(guess[i] == word[j] and answer[i] == '0' and answer[j] == '0'):
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
            k += 1
            answer[j] = '0'
        i += 1
    

    # count = 0
    # count2 = 0
    # j = 0
    # start_index = 0
    # l = 0
    # word = 'hallo'

    # while(j in range(len(word))):
    #     j = 0
    #     j = word.find(letter, start_index)
    #     if(j >= 0):
    #         count+=1
    #         start_index=j+1
    # j = 0
    # start_index = 0
    # while(j in range(len(guess))):
    #     j = 0
    #     j = guess.find(letter, start_index)
    #     if(j >= 0):
    #         count2+=1
    #         start_index=j+1
    
    # j = 0
    # while(count2 != 0 and count != 0):
    #     start_index = 0
    #     while(j in range(len(word))):
    #         j = 0
    #         j = word.find(letter, start_index)
    #         if(j == i):
    #             answer[i] = 'g'
    #             count-=1
    #             count2-=1
    #             j = 0
    #             break
    #         elif(j >= 0):
    #             start_index=j+1
    #     start_index = 0
    #     j = 0
    #     while(j in range(len(word))):
    #         j = 0
    #         j = word.find(letter, start_index)
    #         if(j >= 0 and answer[i] != 'g'):
    #             answer[i] = 'y'
    #             count-=1
    #             count2-=1
    #             j = 0
    #             break
    #         else:
    #             start_index=j+1

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



if __name__ == "__main__":
    main()