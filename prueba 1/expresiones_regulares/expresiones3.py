import re

text = "reemplazando todas las vocales por el asterisco"

next_text =re.sub("[aeiou]", "*",text)

print(next_text)
