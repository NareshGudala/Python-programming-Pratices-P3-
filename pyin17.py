# Python : Remove all whitespace from a string

import re

text="Python      life"
print("Original text:",text)
print("without white space:",re.sub(r'\s+','',text))