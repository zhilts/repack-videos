#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

from lookup import get_files
from transform import transform
from utils import copy_date

parser = argparse.ArgumentParser(description="Reduce video size")
args = parser.parse_args()

OUT_DIR_NAME = "ff_out"


def get_dest_filename(filepath, base_path):
    relative_path = os.path.relpath(filepath, base_path)
    output_path = os.path.join(base_path, OUT_DIR_NAME, relative_path + ".mp4")
    if os.path.exists(output_path):
        raise FileExistsError
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    return output_path


def update_extension(filepath):
    pre, _ = os.path.splitext(filepath)
    os.rename(filepath, pre + ".mp4")


def process_one(index, count, filepath, base_path):
    print("\n" * 3 + "-" * 80)
    print(f"NEXT FILE {index + 1}/{count}: {filepath}")
    out_filename = None
    try:
        out_filename = get_dest_filename(filepath, base_path)
        copy_date(filepath, out_filename)
        transform(filepath, out_filename)
    except FileExistsError:
        print(f"File {filepath} exists in output path. Skipping")
    except BaseException as ex:
        print(ex)
        os.remove(out_filename)


def main():
    base_path = os.getcwd()
    out_out = os.path.join(base_path, OUT_DIR_NAME)
    files = sorted(get_files(base_path, [out_out]))
    count = len(files)
    for index, file in enumerate(files):
        process_one(index, count, file, base_path)


if __name__ == "__main__":
    main()
