import re
import arrow
import datetime
from dateutil.parser import parse


def timestamp_to_datetime(timestamp):
    """
        Converts a unix timestamp to datetime
    """
    return arrow.get(int(timestamp) / 1000.0).datetime


def timestamp_to_isoformat(timestamp):
    """
        Converts a unix timestamp to datetime
    """
    return arrow.get(int(timestamp) / 1000.0).isoformat()



def param_bool(b):
    """
        Converts True and False to true and false
        for passing to the IEX API.
    """
    return str(b == True).lower()


def parse_date(date):
    """
        Parses a date and returns it as YYYYMMDD
        If not parsable, returns False

        Args:
            date
    """
    try:
        return parse(date).strftime("%Y%m%d")
    except ValueError:
        return False


#============#
# Validators #
#============#

def validate_date_format(date_format):
    """
        This function validates the date format specified
        and returns it as a result.
    """
    if date_format not in ['timestamp', 'datetime', 'isoformat']:
        raise ValueError("date_format must be 'timestamp', 'datetime', or 'isoformat'")
    date_format = None if date_format == 'timestamp' else date_format
    return date_format


def validate_range_set(range, range_set):
    """
        Validates that an appropriate range has been passed.

        range - the Range to be tested.
        range_set - the available range options. If 'date' is an option,
                    test for YYYYMMDD.
    """
    passing_criteria = []
    if 'date' in range_set:
        passing_criteria.append(type(range) == datetime.datetime)
        passing_criteria.append(re.match('^[0-9]{8}$', str(range)))
    passing_criteria.append(range in range_set)
    if not any(passing_criteria):
        if 'date' in range_set:
            range_set[range_set.index('date')] = 'YYYYMMDD (int), datetime'
        err_msg = f"Invalid range: '{range}'. Valid chart types are {', '.join(range_set)}"
        raise ValueError(err_msg)
    else:
        url = f"chart/{range}"

