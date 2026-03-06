import re


text = "my_name_is_python and i_like_data_science. this_task_is_about_string_conversion and learning_python_programming."
pattern = r"_"
x = re.findall(pattern, text)
print(text.index("_"))
while "_" in text:
    print(text[text.index("_") + 1], text[text.index("_") + 1].upper())
    text = text[0: (text.index("_") + 1)] + text[text.index("_") + 1].upper() + text[(text.index("_") + 2):]
    text = text.replace("_", "", 1)

print(text)