import sys

file_name = ""
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    raise Exception("No file name provided")

file = open(file_name, "r")
file_content = file.read()
file.close()


