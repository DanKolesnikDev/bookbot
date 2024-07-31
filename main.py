def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)

    print(f"{number_of_words} words found in the document")


# opens book as a string from books directory
def get_book_text(path):
    with open(path) as f:
        return f.read()

# function that counts how many words is in the book  
def get_number_of_words(text):
    words = text.split()
    return len(words)

    
main()

