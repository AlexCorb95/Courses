# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with FileManager("fisier.txt", "w") as f:
#     f.write("We wrote in the file with our own Context Manager")

# from contextlib import contextmanager
#
#
# @contextmanager
# def file_manager(filename, mode):
#     f = open(filename, mode)
#     yield f
#     f.close()
#
#
# with file_manager("test.txt", "w") as f:
#     f.write("We wrote in the file with our own Context Manager which is a function")

# import contextlib
#
#
# @contextlib.contextmanager
# def open_file(filename):
#     f = open(filename, "w")
#     try:
#         yield f
#     finally:
#         f.close()
#
#
# with open_file("test2.txt") as f:
#     f.write("Hellooo !!")
