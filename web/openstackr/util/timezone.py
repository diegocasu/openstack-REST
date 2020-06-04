from datetime import timedelta


def convert_to_utc(localtime, timezone):
    return localtime - timedelta(hours=timezone)