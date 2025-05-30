from stats import get_num_words, get_character_count

import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		num_words = get_num_words(sys.argv[1])
		print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")	
	
		num_chars = get_character_count(sys.argv[1])
		for char in num_chars:
			print(f"{char}: {num_chars[char]}")
		print("============= END ===============")
main()
