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

    # TODO: Return metadata of the selected image in file_name


get_metadata([('Image files', '*.jpg *.pong *.gif *.jpeg'),('Python files', "*.py")])
