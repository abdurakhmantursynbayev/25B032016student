import re

# match = re.match(r"Hello", "Hello world")
# print(match.group())

# match = re.match(r"abdu", "abdurakhman 28 ")
# print(match.group())



# fullmatch checks the WHOLE string, not just a part of it
# print(re.fullmatch(r'\d\d\D\d\d', '12-12'))     # match  -> YES
# print(re.fullmatch(r'\d\d\D\d\d', 'Т. 12-12'))  # None   -> NO

# def validate(pattern, value):
#     return 'YES' if re.fullmatch(pattern, value) else 'NO'

# print(validate(r'[a-z]+', 'hello'))    # YES
# print(validate(r'[a-z]+', 'Hello'))    # NO  (has uppercase)
# print(validate(r'\d{4}', '2026'))      # YES
# print(validate(r'\d{4}', '26'))        # NO  (not exactly 4 digits)


# re.search

# match = re.search(r"hello", "tn tn tn hello world")
# print(match.start())
# print(match.group())
# print(match.end())


# findall

# text = "cat bat sat mat"
# matches = re.findall(r"\bat\b", text)
# print(matches)  # []  — "at" alone doesn't appear

# matches = re.findall(r"\w+at", text)
# print(matches)  # ['cat', 'bat', 'sat', 'mat']

# # Find all dates in text
# text2 = 'Written on 19.01.2018, updated on 01.09.2024'
# print(re.findall(r'\d{2}.\d{2}\.\d{4}', text2))
# # ['19.01.2018', '01.09.2024']




#finditer

text = 'Written on 19.01.2018, updated on 01.09.2024'
for m in re.finditer(r'\d\d\.\d\d\.\d{4}', text):
    print(f'Date {m[0]} starts at position {m.start()}')  # m.group()   or m[0]
# Date 19.01.2018 starts at position 11
# Date 01.09.2024 starts at position 34


#split

txt = "The          rain     in      Spain"

# Split by any whitespace sequence
print(re.split(r'\s+', txt))
# ['The', 'rain', 'in', 'Spain']

# Split by non-word characters (punctuation, spaces, etc.)
print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
# ['Где', 'скажите', 'мне', 'мои', 'очки', '']


#sub

text = "I love cats. Cats are great. My cat is named Whiskers."
result = re.sub(r"[Cc]at", "dog", text)
print(result)
# I love dogs. dogs are great. My dog is named Whiskers.

# Limit replacements with count parameter
result = re.sub(r"[Cc]at", "dog", text, count=1)
print(result)
# I love dogs. Cats are great. My cat is named Whiskers.


text = "I have a super ax and with it you can work. Ax is weapon"
output = re.sub(r"[Aa]x", "power", text)
print(output)