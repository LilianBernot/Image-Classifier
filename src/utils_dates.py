from datetime import datetime
from env import PERIOD

def convert_str_to_datetime(date) -> datetime:
    # Convert the strings to datetime objects
    try:
        date_format = "%Y-%m-%d"  # Format matches "YYYY-MM-DD"
        return datetime.strptime(date, date_format)
    except ValueError:
        date_format = "%Y:%m:%d"  # Format matches "YYYY:MM:DD"
        return datetime.strptime(date, date_format) 

def check_date_is_in_period(period:tuple[datetime, datetime], date:str | datetime | None) -> bool:

    if not date:
        return False
    
    if isinstance(date, str):
        date = convert_str_to_datetime(date) 

    is_sup = period[0] <= date
    is_inf = date < period[1]

    return is_sup and is_inf

def get_fitting_periods(periods_list: list[PERIOD], dates:list[str|None]) -> list[PERIOD | None]:

    periods_list_datetime: list[tuple[datetime, datetime]] = []
    for start, end, _ in periods_list:
        periods_list_datetime.append((convert_str_to_datetime(start), convert_str_to_datetime(end)))

    fitting_periods:list[PERIOD | None] = []
    for date in dates:
        fitting_period = None
        for index, period in enumerate(periods_list_datetime):
            if check_date_is_in_period(period, date):
                fitting_period = periods_list[index]

        fitting_periods.append(fitting_period)
    
    return fitting_periods