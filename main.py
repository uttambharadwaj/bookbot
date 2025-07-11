from stats import get_book_length, get_character_frequency
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at: {file_location}")
        print("----------- Word Count ----------")
        print(f"Found {get_book_length(file_location)} total words")
        print("--------- Character Count -------")
        text = get_character_frequency(file_location)
        for i in text:
            print(f"{i[0]}: {i[1]}")
        print("============= END ===============")
      
if __name__ == "__main__":
    main()
