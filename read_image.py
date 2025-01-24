import os
from PIL import Image
from PIL.ExifTags import TAGS
from read_periods import get_periods, get_period_folder_name
from utils_dates import get_fitting_periods
from env import PERIOD
from move_file import move_file

# Specify the folder path
folder_path = "./data"

def get_datetime_image(image_path:str) -> str | None:
    # open the image
    image = Image.open(image_path)
    
    # extracting the exif metadata
    exifdata = image.getexif()

    if exifdata:
        for tag_id, value in exifdata.items():
            # Get the tag name
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTime":  # This is the creation date tag
                return value[:10]
    
    return None


# Iterate through all files in the folder
def get_periods_from_images(folder_path, images: list[str]) -> list[PERIOD | None]:
    
    dates: list[str|None] = []
    for image_name in images:
        image_path = os.path.join(folder_path, image_name)
        dates.append(get_datetime_image(image_path))

    periods = get_periods('periods.txt')

    fitting_periods = get_fitting_periods(periods_list=periods, dates=dates)

    return fitting_periods

def get_periods_folder_images(folder_path: str):

    explored_images: list[str] = []
    for image_name in os.listdir(folder_path):
        explored_images.append(image_name)

    fitting_periods = get_periods_from_images(folder_path, explored_images)

    issues: list[str] = []
    for index, image_name in enumerate(explored_images):
        period = fitting_periods[index]
        if not period:
            issues.append(os.path.join(folder_path, image_name))
        else:
            fitting_folder = get_period_folder_name(period)
            move_file(os.path.join(folder_path, image_name), os.path.join(fitting_folder, image_name))

    if issues:
        print(f"We got issues with the following images : {issues}. Impossible to find a corresponding period.")
    else:
        print("No issues, all images moved correctly !")

get_periods_folder_images(folder_path)