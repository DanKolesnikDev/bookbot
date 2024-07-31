def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    count_characters = get_count_charactes(text)

    print(f"{number_of_words} words found in the document")
    print(f"counted how many times apears every character in document: {count_characters}")


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
    lowered_text = text.lower()
    char_list = list(lowered_text)
    chars = set(char_list)

    for char in chars:
        char_count[char] = 0

    for char in char_list:
        char_count[char] += 1
    return char_count
    
main()

