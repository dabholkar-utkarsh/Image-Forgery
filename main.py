from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import exifread
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def get_metadata(file_types=[('Image files', '*.jpg *.pong *.gif *.jpeg')]):
    """
        opens up a file chooser to select an image file
        :return: metadata of the selected file
    """
    Tk().withdraw()
    file_name = askopenfilename(title="Select an image", filetypes=file_types)
    print(file_name)
    parser = createParser(file_name)
    for line in extractMetadata(parser).exportPlaintext():
        print(line)
    with open(file_name, "rb") as f:
        tags = exifread.process_file(f)
        #print(tags)
        print('$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(tags['Image Software'])
        print('$$$$$$$$$$$$$$$$$$$$$$$$$')


get_metadata()





