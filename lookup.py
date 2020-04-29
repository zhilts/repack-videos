import os
import re

from utils import wrap_result


def include(filepath, exclude):
    for exclusion in exclude:
        if filepath.startswith(exclusion):
            return False
    return re.compile(r".*(\.avi|\.mov|.mp4|.mpg|.mkv)$", re.IGNORECASE).match(filepath)


@wrap_result(tuple)
def get_files(base_path, exclude):
    for root, dirs, files in os.walk(base_path, followlinks=True):
        for filename in files:
            filepath = os.path.join(root, filename)
            if include(filepath, exclude):
                yield filepath
