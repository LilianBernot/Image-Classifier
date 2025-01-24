import os
from PIL import Image
from PIL.ExifTags import TAGS
from read_periods import get_periods
from utils_dates import get_fitting_periods
from env import PERIOD

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
def get_periods_from_images(images: list[str]) -> list[PERIOD | None]:

    dates: list[str|None] = []
    for image_path in images:
        dates.append(get_datetime_image(image_path))

    periods = get_periods('periods.txt')

    fitting_periods = get_fitting_periods(periods_list=periods, dates=dates)

    return fitting_periods

def get_periods_folder_images(folder_path: str):

    explored_images: list[str] = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        explored_images.append(file_path)

    fitting_periods = get_periods_from_images(explored_images)

    print(fitting_periods)

get_periods_folder_images(folder_path)