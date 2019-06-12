import os
import platform
from datetime import datetime
from functools import wraps
import subprocess

__all__ = [
    "wrap_result",
    "copy_date",
]

def wrap_result(wrapper_fn):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            result = fn(*args, **kwargs)
            return wrapper_fn(result)

        return decorator

    return wrapper


def copy_date(src, dist):
    timestamp = creation_date(src)
    timestamp_format = datetime.fromtimestamp(timestamp).strftime("%Y%m%d%H%M.%S")
    subprocess.run([
        "touch",
        "-t", timestamp_format,
        dist
    ])


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
