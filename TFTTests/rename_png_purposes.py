import os

os.getcwd()
collection = (r"C:/Users/XXX/Desktop/py_test/champs/")

for i, filename in enumerate(os.listdir(collection)):
    head,body,tail = filename.partition('_')
    os.rename(r"C:/Users/XXX/Desktop/py_test/champs/" + filename, r"C:/Users/XXX/Desktop/py_test/champs/" + head + ".png")