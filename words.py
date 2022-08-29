def print_upper_words(words_list, letter_list):
    ''' Prints words in words_list uppercase if they begin with a letter from letter_list '''
    for letter in letter_list:
        for word in words_list:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ['h', 'g'])