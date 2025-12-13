#write a program to fill a letter template given below with name and date.
letter ='''dear <|name|>,
you are selected!
<|date|>'''
print(letter.replace("<|name|>","abhishek").replace("<|date|","13 december 2025"))