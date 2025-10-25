# f = open("data/text.txt", 'r')
# print(f.read())
# f.close()
import warnings

# with open('data/text.txt', 'r') as f:
#     for line in f:
#         print(line, end="")

# with open("data/text.txt", "a") as text_file:
#     text_file.write("my name is\n")
#
# with open("data/text.txt", "r") as text_file:
#     for line in text_file:
#         print(line.strip())

#HW 1.1
# names = ["Alice", "Bob", "Charlie", "Denis", "Eve", "Mary"]
# with open("data/users.txt", "w") as f:
#  f.writelines(name + "\n" for name in names)

#HW 2.1
# import os
# path = "data/users.txt"
# if os.path.exists(path):
#     with open(path, "r", encoding="utf-8") as text_file:
#         lines = [line.strip() for line in text_file]
#         print(len(lines))
#         name_filter = [name for name in lines if name.startswith(("C", "D"))]
#         print(name_filter)
# else:
#     print("File not found")

#HW 3.1
#
# warning_list = ["Error: file not found", "Warning: low memory", "Info: process started", "Error: no path"]
# with open("data/log.txt", "w", encoding="utf-8") as f:
#     for line in warning_list:
#         f.write(line + "\n")
#
# with open("data/log.txt", "r", encoding="utf-8") as f:
#     err_filter = [line.strip() for line in f if line.startswith("Error")]
#     print(err_filter)

#HW 4.1
# with open("data/a.txt", "r", encoding="utf-8") as f_a:
#     data1 = f_a.read()
#
# with open("data/b.txt", "r", encoding="utf-8") as f_b:
#     data2 = f_b.read()
#
# with open("data/combined.txt", "w", encoding="utf-8") as f_c:
#     f_c.write(data1 + data2)

