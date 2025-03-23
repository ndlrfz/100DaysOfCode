import os


def rename_files():
    file_list = os.listdir(r"/home/ndlr/Desktop/wall")
    saved_path = os.getcwd()
    print(file_list)
    print(os.getcwd())

rename_files()
