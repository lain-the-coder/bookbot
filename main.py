import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
from stats import sort_dict
from stats import count_characters
from stats import count_words

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_path = sys.argv[1]
	content = get_book_text(book_path)
	print("============ BOOKBOT ============")
	print("Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	words = count_words(content)
	print(f"Found {words} total words")
	chara = count_characters(content)
	print("--------- Character Count -------")
	sorted_list = sort_dict(chara)
	for item in sorted_list:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

if __name__ == "__main__":
	main()
