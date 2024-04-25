from mid_night_test import word_counter
from mid_night_test import first_two
from mid_night_test import add_words

def test_mid_night_snacks_count():
	assert word_counter('semicolon') == 9

def test_mid_night_snacks_one():
	assert first_two('semicolon') == 'seon'
	assert first_two('o') == ""
	assert first_two('on') == 'onon'
	
def test_mid_night_snacks_add():
	assert add_words('se') == 'se'
	assert add_words('seming') == 'semingly'
	assert add_words('sem') == 'seming'


