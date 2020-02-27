from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames


def get_forgery_software():
    """

    :return: !!list of forgery software!!
    """
    with open("forgery_software.txt") as f:
        return [line.rstrip("\n") for line in f.readlines()]


forgery_list = get_forgery_software()


def get_file_name(file_types=[('Image files', '*.jpg *.png *.gif *.jpeg')]):
    """"
        opens up the file in which the image exists
        :returns image location
    """

    Tk().withdraw()
    return askopenfilename(title="Select an image", filetypes=file_types)


def get_metadata(filename):
    """"
    :returns metadata of image
    """
    parser = createParser(filename)
    metadata = extractMetadata(parser).exportPlaintext()
    metadata = metadata[1:]
    meta_dictionary = {}
    for element in metadata:
        element = element.strip("- ")
        index = element.index(": ")
        key = element[:index]
        value = element[index + 2:]
        meta_dictionary[key] = value
    # Printing meta data
    print("""
==========
Meta Data
==========
""")
    for key, value in meta_dictionary.items():
        print(key, ":", value)
    # Checking if key producer is available to check for forgery
    try:
        return meta_dictionary["Producer"]
    except KeyError as ex:
        return -1


def find_forgery(file_name):

    metadata = get_metadata(file_name)

    if metadata == -1:
        print("\n\nResult: Image may not be forged")
        exit(0)

    forged = False  # boolean value initialised

    for element in forgery_list:
        if element in metadata.lower():
            forged = True
            break

    print("\n\nResult:", end=" ")
    if forged:
        print("The image may be forged using", str(metadata)+".")
    else:
        print("The image may not be forged.")


find_forgery(get_file_name())
