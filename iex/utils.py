import re
import arrow
import datetime
from dateutil.parser import parse
from iex.constants import DATE_FIELDS


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


def convert_pandas_datetimes(df, date_format):
    """
        Converts columns in pandas dataframe
    """
    date_field_conv = [x for x in df.columns if x in DATE_FIELDS]
    if date_field_conv:
        date_apply_func = None
        if date_format == 'datetime':
            date_apply_func = timestamp_to_datetime
        elif date_format == 'isoformat':
            date_apply_func = timestamp_to_isoformat
        if date_apply_func:
            df[date_field_conv] = df[date_field_conv].applymap(date_apply_func)
    return df




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
        parsed_date = parse(str(date))
    except ValueError:
        return False
    if (arrow.now().date() - parsed_date.date()).days < 0:
            raise ValueError("Date cannot be set in the future")
    return parsed_date.strftime("%Y%m%d")


#============#
# Validators #
#============#

def validate_output_format(output_format):
    if output_format not in ['dataframe', 'json']:
        raise ValueError("batch format must be either 'dataframe' or 'json")
    return output_format


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
        passing_criteria.append(parse_date(range))
    passing_criteria.append(range in range_set)
    if not any(passing_criteria):
        if 'date' in range_set:
            range_set[range_set.index('date')] = 'YYYYMMDD (int), datetime'
        err_msg = f"Invalid range: '{range}'. Valid chart types are {', '.join(range_set)}"
        raise ValueError(err_msg)
    else:
        url = f"chart/{range}"

