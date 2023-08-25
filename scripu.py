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
        default='1',
        dest='output_dir',
        type=str,
        help='',
    )

    #return parser.parse_args()
    return parser


if __name__ == "__main__":
    print(_parse_args()._actions)
