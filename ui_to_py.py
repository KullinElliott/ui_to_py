"""
This module function converts .ui file(s) to .py files.

Functions:
    convert(file_name, directory_ui, directory_py)

Variables:
    file_name: str
    directory_ui: str
    directory_py: str
    cwd: str
    path: str
    path_py: str
    path_ui: str

"""
import os
import subprocess


def convert(file_name: str, directory_ui: str, directory_py: str):
    """
    Converts .ui files to .py files given the filename and directory it is located.

    Parameters:
        :param file_name:
            current file name of the '.ui' and name used for the created '.py' file
        :param directory_ui:
            current folder location of the '.ui' file to be converted
        :param directory_py:
            location the created '.py' file will be saved to post conversion

    Returns:
        Nothing is returned, file are converted from '.ui' to '.py' for use in the main programs
    """
    path_ui = os.path.join(directory_ui, file_name + '.ui')
    path_py = os.path.join(directory_py, file_name + '.py')

    subprocess.call(["pyuic5", path_ui, "-o", path_py])

'''
filename = 'mw_Main'
print(filename)
convert(filename)

filename = 'QtDialogWindowStep_3_Doric'
print(filename)
convert(filename)


for i in range(1, 7):
    filename = ('QtDialogWindowStep_{}'.format(i))
    print(filename)
    convert(filename)
'''
