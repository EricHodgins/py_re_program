# coding: utf-8
import re
from sys import exit

class Person(object):

	def __init__(self, **kwargs):
		self.attributes = []
		for key, value in kwargs.items():
			setattr(self, key, value)
			self.attributes.append(value)

	def __str__(self):
		return "First Name:<{}>, Last Name:<{}>, email:<{}>, phone:<{}>, job:<{}>, twitter:<{}> ".format(self.first, self.last, self.email, self.phone, self.job, self.twitter)





with open("names.txt") as open_file:
	data = open_file.read()


#print data
# get each persons first, last name, e-mail, phone number, work, and Twitter info
parsed_data = re.compile(r'''
	^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t
	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t?\s?
	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t
	(?P<job>[\w.\s]+,[\w.\s]+)\t?
	(?P<twitter>@[\w\d.]+)?$
''', re.X|re.M)

#print parsed_data.search(data).groupdict()
people = (parsed_data.findall(data))

#for person in people:
#	print(person)
people = []
for match in parsed_data.finditer(data):
	new_person_class = match.group('first')
	new_person_class = Person(**match.groupdict())
	people.append(new_person_class)

count = 0
for person in people:
	#print(person.attributes) 
	count += 1

#print("The count is {}".format(count))

while True:
	search_item = input("[Q]uit or Enter what you would like to find: ")
	if search_item.upper().strip()[0] == 'Q':
		exit(0)

	for person in people:
		for person_info in person.attributes:
			try:
				if re.search(search_item, person_info) != None:
					print(person)
					print("\n")
					break
			except:
				continue



# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character.
# \W - is the opposite and matches anything that isn't an Unicode word character.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches things that aren't the edges of a word.

# \w{3} - matches any three word characters in a row.
# \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# \w? - matches 0 or 1 word characters.
# \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.
# ? means optional

# [^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
# re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
# re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.


# ([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
# (?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
# .groups() - method to show all of the groups on a Match object.
# re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
# ^ - specifies, in a pattern, the beginning of the string.
# $ - specifies, in a pattern, the end of the string.
