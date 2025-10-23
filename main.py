# python
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path=sys.argv[1]

from stats import word_count, char_numbs, sorted_char

def get_book_text(file_path):

    #Open the file
    with open(file_path) as b:

    #Read the file
        book_text = b.read()

    #count the words in the text
    wcount = word_count(book_text)
    #count the total number of each letter in the text  
    chars = char_numbs(book_text)
    #print out the letters
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")
    print("--------- Character Count -------")
    in_order = sorted_char(chars)
    for item in in_order:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
   



def main():
    get_book_text(sys.argv[1])
    

main()