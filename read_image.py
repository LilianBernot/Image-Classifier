import os
from PIL import Image
from PIL.ExifTags import TAGS

# Specify the folder path
folder_path = "./data"

def print_datetime_image(image_path):
    # open the image
    image = Image.open(image_path)
    
    # extracting the exif metadata
    exifdata = image.getexif()

    if exifdata:
        for tag_id, value in exifdata.items():
            # Get the tag name
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTime":  # This is the creation date tag
                print(f"Image creation date : {value}")



# Iterate through all files in the folder
def print_datetimes_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            print_datetimes_folder(file_path)
            return

        print_datetime_image(file_path)

print_datetimes_folder(folder_path)