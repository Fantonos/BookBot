
# Main function, creates variables and runs functions
def main():
    book_path = "books/frankenstein.txt"
    word_count = num_of_words(book_path)
    print_word_count(word_count[0], word_count[1], book_path)


#gets the entire book and returns it as f
def get_book_text(path):
    with open(path) as f:
        return f.read()


#Take in the book and create the word count and dic
def num_of_words(path):
    character_count_dic = {}
    word_count = (get_book_text(path)).lower().split()
    for char in word_count: #Lists every word(char) in word word_count
        letters = list(char) #splits word into a list containing each letter
        for let in range(0, len(letters)): 
            if letters[let].isalpha(): #checks to see if they are alpha(in alphabet)
                character_count_dic[letters[let]] = character_count_dic.get(letters[let], 0) + 1 #if value of key = none then key is 0 else key + 1

    return [len(word_count), dict(sorted(character_count_dic.items(), key=lambda item: item[1], reverse=True))] #LOL just sorts a dic

#prints the final message to the console
def print_word_count(word_count, letter_dic, path_2_book):
    print(f'--- Begin report of {path_2_book} --- \n{word_count} words found in the document \n')
    for char in letter_dic:
        print(f"The '{char}' character was found {letter_dic[char]} times")
    print(f'--- End report ---')


main()