#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo ligand CCD definition parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
# File IO class, read and write mmcif file

filepath = "structure_files/2hyv.cif"
io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

coordinates = data_container.getObj('atom_site')
# obtain data category from data container

n_rows = coordinates.getRowCount()
# get number of data record rows

# for i in range(n_rows):
#     d_row = coordinates.getRowAttributeDict(i)
#     if d_row["label_comp_id"] == "CA":
#         print("auth_comp_id: %s; auth_asym_id: %s; auth_seq_id: %s" % (
#             d_row["auth_comp_id"], d_row["auth_asym_id"], d_row["auth_seq_id"]))

l_index = coordinates.selectIndices("CA", "label_comp_id")
for i in l_index:
    d_row = coordinates.getRowAttributeDict(i)
    print("res: %s; chain: %s; seq: %s" % (
        d_row["auth_comp_id"], d_row["auth_asym_id"], d_row["auth_seq_id"]))
