def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    count_characters = get_count_charactes(text)
    sorted_characters = sort_on(count_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    for c in sorted_characters:
        print(f"The {c["char"]} character was found {c["num"]} times")
    print("--- End report ---")


# opens book as a string from books directory
def get_book_text(path):
    with open(path) as f:
        return f.read()

# function that counts how many words is in the book  
def get_number_of_words(text):
    words = text.split()
    return len(words)

# counts lowercase all characters and counts how many of each chartacter is in the book
# returns as dictionary character > count
def get_count_charactes(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 0
    return char_count

# sorts all characters from most used in document to least
def sort_on(characters):
    list_of_char = [{"char" : key, "num": value} for key, value in characters.items()]
    list_of_char.sort(reverse=True, key=lambda x: x["num"])
    return list_of_char
    

    
main()

