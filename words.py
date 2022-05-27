def print_upper_words(words_list):
    '''this should print out each word on its own line and in uppercase'''
    words = words_list
    for word in words:
        print(word.upper())

print_upper_words(["hey", "hi", "hello", "yo", "sup"])

def print_upper_words_two(words_list):
    words = words_list
    for word in words:
        if word.startswith('h') or word.startswith("H"):
            print(word.upper())

print_upper_words_two(["hey", "Hi", "hello", "yo", "sup"])

def print_upper_words_three(words_list, first_set, second_set):
    words = words_list
    for word in words:
        if word.startswith(first_set) or word.startswith(second_set):
            print(word.upper())

print_upper_words_three(["hey", "hi", "hello", "yo", "sup"], "h", "s")
