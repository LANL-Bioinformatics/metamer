#!/usr/bin/env python

"""Tests for `meta mash` package."""

import pytest
import os
import sys
import luigi
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.abspath(os.path.join(dir_path, '..'))
bin_path = os.path.join(lib_path, 'bin')
sys.path.append(lib_path)
os.environ["PATH"] += os.pathsep + bin_path
from metamer import sketch, dist

def test_CalculateDist(tmpdir):
    """
    Test if this first luigi class works

    test for creating matrix of mash distances

    """

    luigi.interface.build([sketch.AllSketches(data_folder="tests/data/fqs",
                              kmer=31, threads=2, sketch=100,
                              seed=2500, min_copy=2, out_dir="tests/sk_test",
                              mash_tool="mash")],
                          local_scheduler=True, workers=1)
    luigi.interface.build([dist.Alldist(data_folder="tests/mds", threads=2,
                                        out_file="tests/test_table.txt")],
                          local_scheduler=True, workers=1)

    file_basenames = [os.path.basename(x) for x in tmpdir.listdir()] 
    assert 'tests/test_table.txt' in file_basenames
