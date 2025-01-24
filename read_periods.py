import re
import os

# Path to the periods file
periods_file = "periods.txt"

def get_periods(periods_file):

    # Regular expression to match the date range: "YYYY-MM-DD to YYYY-MM-DD"
    date_pattern = r"(\d{4}-\d{2}-\d{2})\s+to\s+(\d{4}-\d{2}-\d{2})"
    # regular expression to match the location "= Location"
    location_pattern = r"=\s*(.+)"

    # List to store the extracted date periods
    date_periods = []

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

            date_periods.append((start_date, end_date, location))

    return date_periods

def create_periods_folders(periods_data:list[tuple[str, str, str]]):

    for start, end, location in periods_data:
        if location:
            # convert tolcation to Snakecase
            newpath = location[0].upper() + location[1:].lower()
        else:
            newpath = start + '_' + end

        if not os.path.exists(newpath):
            os.makedirs(newpath)

create_periods_folders(get_periods(periods_file))