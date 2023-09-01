import argparse
import shutil

import json
from pathlib import Path


def _parse_args():
    parser = argparse.ArgumentParser(description='Tool to merging two logs.')

    parser.add_argument(
        'input_log1',
        metavar='<INPUT LOG FILE>',
        type=str,
        help='path to first file with generated logs for merging',
    )

    parser.add_argument(
        'input_log1',
        metavar='<OUTPUT DIR>',
        type=str,
        help='path to first file with generated logs for merging',
    )

    parser.add_argument(
        '-o', '--output',
        action='store',
        dest='output_dir',
        type=str,
        help='path to new merged log file',
    )

    

    return parser.parse_args()


def _create_dir(dir_path: Path, *, force_write: bool = False) -> None:
    if dir_path.exists():
        if not force_write:
            raise FileExistsError(
                f'Dir "{dir_path}" already exists. Remove it first or choose another one.')
        shutil.rmtree(dir_path)

    dir_path.mkdir(parents=True)


def _create_new_log():

if __name__ == "__main__":
    print()
