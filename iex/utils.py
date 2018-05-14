import arrow
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
