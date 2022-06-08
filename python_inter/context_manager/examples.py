# f = open("file.txt", 'w')
# try:
#     f.write("Hello world")
#     # f.write(Hello)
# except NameError:
#     print("Error occured")
# finally:
#     print("The file will be closed")
#     f.close()

with open("file.txt", "w") as f:
    f.write("Hello world !!")
