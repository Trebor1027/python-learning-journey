import re

text = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dogs$",text)

if x:
    print("Si")
else:
    print("No")
    