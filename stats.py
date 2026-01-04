# Takes a relative file path and converts its contents into a useable string
def get_book_text_count(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    
    word_count =  file_contents.split()
    
    return word_count


# Converts an input string into a dictionary counting the number of times each character appears
def count_characters(string):
    character_count = {}
    book_string = ""
    
    for str in string:
        book_string += str

    for char in book_string:
        character = char.lower()
        is_char_present = character in character_count

        if is_char_present == False:
            character_count[character] = 1
        else:
            character_count[character] += 1
        
    return character_count


def get_num_key(dict):
    num_key = dict["num"]
    return num_key


def sort_dictionary(dictionary):
    sorted_list = []
    char_dict = {}

    for i in dictionary:
        char_dict["char"] = i
        char_dict["num"] = dictionary[i]
        sorted_list.append(char_dict)
        char_dict = {}

    sorted_list.sort(reverse=True, key=get_num_key)
    return sorted_list