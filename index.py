import os
baseDir = os.path.abspath(os.path.dirname(__file__))
# print(baseDir)

file_path = os.path.join(baseDir, "zen_of_python.txt")
# print(file_path)

file_obj = open(file_path)

with open(file_path) as file_obj:
    file_content_read_line =  file_obj.readline()
    print(file_content_read_line[-1])

fileContentReadlines = file_obj.readlines()
# print(fileContentReadlines)

is_better_than_count = 0

for element in fileContentReadlines:
    if "is better than" in element:
        is_better_than_count += 1
   
print(is_better_than_count)
file_obj.seek(1)

fileContentReadlines2 = file_obj.readlines()
# print("This is the second attempt",fileContentReadlines2)