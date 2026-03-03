import re

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string\

text = "Hello, my email is student@kbtu.kz"
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
print(match.group())  # student@kbtu.kz

# .	Any character except newline	a.c	abc, a1c, a c
# ^	Start of string	^Hello	Hello world
# $	End of string	world$	Hello world
# |	OR	cat|dog	cat or dog
# ()	Group	(ab)+	ab, abab
# \	Escape special character	\.	literal .


# *	0 or more
# +	1 or more
# ?	0 or 1 (optional)
# {n}	Exactly n times
# {n,}	n or more times
# {n,m}	Between n and m times


tt = "abdurakhman said hello world"
pattern = r"(\b\w+\b)\s(\w+\b)"
matchh = re.search(pattern, tt)
print(matchh.group(0))
print(matchh.group(1))
print(matchh.group(2))
