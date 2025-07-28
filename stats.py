def sort_dict(dict_sort):
	sorted_lst = []
	for char, count in dict_sort.items():
		if char.isalpha():
			sorted_lst.append({"char": char, "num": count})
	def sort_on(item):
		return item["num"]
	sorted_lst.sort(reverse=True, key=sort_on)
	return sorted_lst


def count_characters(content):
	content = content.lower()
	char_count = {}
	for char in content:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count


def count_words(content):
        word_count = 0
        for word in content.split():
                word_count += 1
        return word_count
