file_name = input('Enter file name : ')
d =	{"py": "Python", "txt": "Text", "zip": "Compressed File"}
ext = file_name.split(".")[-1]
print(d[ext])