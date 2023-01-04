import os

current_dir = os.getcwd()
new_folder_path = os.path.join(current_dir, "new_folder")


def make_dir(dir_name):
    destination_folder = os.path.join(new_folder_path, dir_name)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    return destination_folder


def check_ext(extn):
    for path, dirname, filename in os.walk(current_dir):
        for f1 in filename:
            if os.path.splitext(f1)[-1] == f".{extn}":
                os.rename(os.path.join(path, f1), os.path.join(make_dir(f"{extn}_file"), f1))


check_ext("txt")
check_ext("docx")
check_ext("jpg")
