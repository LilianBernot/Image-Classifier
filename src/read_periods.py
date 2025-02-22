import re
import os
from env import PERIOD

def check_overlapping_periods(periods:list[PERIOD]):
    """
    Checks that the defined periods are not overlapping.
    We check that we don't have : 
        - start date > end date for a given period (not a reversed period)
        - if start_i < start_j, then end_i < end_j (periods do not cross)
    """
    for i in range(len(periods)):
        if periods[i][0] > periods[i][1]:
            raise ValueError(f"Period {periods[i]} has end date before starting date !")

    periods.sort(key=lambda x: x[0])
    # We sort the periods by the start date

    for i in range(len(periods) - 1):
        if periods[i][1] >= periods[i+1][0]:
            # We want the end date of i to be strictly lower than start date of i+1
            raise ValueError(f"Periods {periods[i]} and {periods[i+1]} are overlapping !")
    

def get_periods(periods_file: str) -> list[PERIOD]:
    """
    Gets periods from the period file.
    Parses the period file to retrieve the periods that are written in the format :
        YYYY-MM-DD to YYYY-MM-DD = Location
    
    Returns : 
        - list[PERIOD] : the list of parsed periods
    """
    # Regular expression to match the date range: "YYYY-MM-DD to YYYY-MM-DD"
    date_pattern = r"(\d{4}-\d{2}-\d{2})\s+to\s+(\d{4}-\d{2}-\d{2})"
    # regular expression to match the location "= Location"
    location_pattern = r"=\s*(.+)"

    # List to store the extracted date periods
    date_periods: list[PERIOD] = []

    # Open and process the file
    with open(periods_file, "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith("#") or not line:  # Skip comments and empty lines
                continue

            # Apply date pattern
            date_match = re.search(date_pattern, line)
            start_date, end_date = date_match.groups() if date_match else (None, None)

            # Apply location pattern
            location_match = re.search(location_pattern, line)
            location = location_match.group(1) if location_match else None

            if not isinstance(start_date, str) or not isinstance(end_date, str):
                raise ValueError(f"The period [{line}] is not recognized.")
            
            date_periods.append((start_date, end_date, location))

    check_overlapping_periods(date_periods)

    return date_periods

def get_period_folder_name(period:PERIOD) -> str:
    """
    Creates a folder name from a period.
    Uses Location if exists, otherwise start_end.

    Returns :
        - str : the created folder name.
    """
    start, end, location = period
    if location:
        # convert tolcation to Snakecase
        newpath = location[0].upper() + location[1:].lower()
    else:
        newpath = start + '_' + end

    return newpath

def create_periods_folders(periods_file:str, root_folder='.'):
    """
    Creates the folders for the given periods at the root_folder.
    """
    periods_data = get_periods(periods_file)
    for period in periods_data:
        newpath = os.path.join(root_folder, get_period_folder_name(period))

        if not os.path.exists(newpath):
            os.makedirs(newpath)