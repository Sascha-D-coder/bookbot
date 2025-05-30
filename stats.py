def get_num_words(path_to_file):
	with open(path_to_file) as f:
       		file_contents = f.read()
	word_split_list = file_contents.split()

	return len(word_split_list)

def get_character_count(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	file_contents = file_contents.lower()
	character_split_list = list(file_contents)
	
	dic_char_count = {}

	for char in character_split_list:
		if char not in  dic_char_count:
			dic_char_count[char] = 0
		if char in dic_char_count:
			dic_char_count[char] += 1
	
	
	return sort_dict(dic_char_count)


def sort_dict(dictionary):
	sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
	return sorted_dict
