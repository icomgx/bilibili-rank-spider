__version__ = '0.1.0'


def utc_to_local_datetime(dt):
    """Converts a naive UTC datetime object to a naive local datetime object."""

    from datetime import datetime
    from flask.ext.babel import format_datetime

    return datetime.strptime(format_datetime(dt, 'YYYY-MM-dd HH:mm:ss'), '%Y-%m-%d %H:%M:%S')


def local_to_utc_datetime(dt):
    """Converts a naive local datetime object to a naive UTC datetime object."""

    from datetime import datetime
    import pytz
    from babel.dates import format_datetime as babel_format_datetime
    from flask.ext.babel import get_timezone as flask_babel_get_timezone

    local = flask_babel_get_timezone()

    return datetime.strptime(babel_format_datetime(local.localize(dt), 'YYYY-MM-dd HH:mm:ss', tzinfo=pytz.UTC), '%Y-%m-%d %H:%M:%S')

