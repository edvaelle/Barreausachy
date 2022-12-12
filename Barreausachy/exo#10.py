import re
text = "Barreau Sachy Edvaelle"

pattern = r"[A-Z]+"

regex = re.findall(pattern,text)
regex = ''.join(regex)
print(regex)

