#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List, Dict
import os
import sys
import subprocess
from collections import defaultdict
from argparse import ArgumentParser


def search_python_version_file(directory: str) -> List[str]:
    '''search .python-version file under the indicated directory
    '''
    if not os.path.exists(directory):
        raise ValueError(f'{directory} is not exists')
    if not os.path.isdir(directory):
        raise ValueError(f'{directory} is not directory')
    cmd = f'find {directory} -name .python-version -print'.split()
    raw_vfiles = subprocess.run(
        cmd, encoding='utf-8', stdout=subprocess.PIPE
    ).stdout.splitlines()
    vfiles = list()
    for rv in raw_vfiles:
        srv = rv.strip()
        if len(srv) == 0:
            continue
        if os.path.isfile(srv):
            vfiles.append(srv)
    if len(vfiles) == 0:
        raise ValueError(f'no Python project under {directory}')
    return vfiles


def read_python_version_file(vfiles: List[str]) -> Dict[str, str]:
    '''read .python-version file and get the name of Python virtualenv
    '''
    vdict = dict()
    for vf in vfiles:
        vdir = os.path.dirname(vf)
        with open(vf, 'rt') as rf:
            vname = rf.readline().strip()
        vdict[vdir] = vname
    return vdict


def print_python_versions(vdict: Dict[str, str]) -> None:
    common_dir = None
    vcount = defaultdict(list)
    # extract common_dir
    for vdir in vdict.keys():
        if common_dir is None:
            common_dir = vdir.split(os.sep)
            continue
        vpath = vdir.split(os.sep)
        for i, cp in enumerate(common_dir):
            if len(vpath) > i and common_dir[i] == vpath[i]:
                continue
            else:
                common_dir = common_dir[:i]
                break
    # print out
    print(f'Search under the directory: {os.sep.join(common_dir)}')
    for vdir, vname in sorted(vdict.items()):
        vtdir = os.sep.join(vdir.split(os.sep)[len(common_dir):])
        if vtdir == '':
            vtdir = '.'
        vcount[vname].append(vtdir)
    for vname, vtdirs in sorted(vcount.items()):
        print(f'{vname} ({len(vtdirs)}):')
        for vtd in sorted(vtdirs):
            print(f'  {vtd}')
    return


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        '-d', '--directory', default='.', type=str,
        help=(
            'the directory you search .python-version files recursively.'
            ' default: "." (current working directory)'
        )
    )
    args = parser.parse_args()
    try:
        vfiles = search_python_version_file(**vars(args))
    except Exception as e:
        print(e)
        sys.exit(1)
    vdict = read_python_version_file(vfiles=vfiles)
    print_python_versions(vdict=vdict)
    return


if __name__ == '__main__':
    main()
