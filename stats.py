word_count = ""
# Takes a relative file path and converts its contents into a useable string
# 
def get_book_text_count(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    
    word_count =  file_contents.split()
    
    return word_count

# Converts an input string into a dictionary counting the number of times each character
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