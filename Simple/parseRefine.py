#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo refinement parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
# File IO class, read and write mmcif file

filepath = "structure_files/2hyv.cif"
io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

refine = data_container.getObj('refine')
# obtain data category from data container

d_refine = refine.getRowAttributeDict(0)
# get 1st data row as dictionary

l_attr = ["ls_d_res_high",
          "ls_R_factor_R_work",
          "ls_R_factor_R_free",
          "pdbx_method_to_determine_struct"]
for attr in l_attr:
    print("%s: %s" % (attr, d_refine[attr]))
