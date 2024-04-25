def word_counter(words):
	return  (len(words))
	
def first_two(words):
	if len(words) < 2:
		return ""
	else:
		return (words[:2]) + (words[-2:]) 

def add_words(words):
	if len(words) < 3:
		result = words
	elif words[-3:] == 'ing':
		result = words + 'ly'
	else: 
		result = words[-3:] + 'ing'
	return result

