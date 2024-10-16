def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words(book_path)
    #print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(path):
    word_count = len((get_book_text(path)).split())
    print(word_count)


main()