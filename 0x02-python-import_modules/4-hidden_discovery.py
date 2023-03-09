#!/usr/bin/python3
import marshal

# import pyc file
s = open("hidden_4.pyc", "rb")
s.seek(16)
code_obj = marshal.load(s)

# protect execution of code if file is imported
if __name__ == "__main__":
    exec(code_obj)

    for i in range(len(code_obj.co_names)):
        if code_obj.co_names[i][i] != "_":
            print("{}".format(code_obj.co_names[i]))
