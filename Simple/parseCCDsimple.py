#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo non-polymer parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
# File IO class, read and write mmcif file

filepath = "ligand_files/ATP.cif"
io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

descriptor = data_container.getObj('pdbx_chem_comp_descriptor')
# obtain data category from data container

n_rows = descriptor.getRowCount()
# get number of data record rows

for i in range(n_rows):
    d_row = descriptor.getRowAttributeDict(i)
    if d_row["type"] == "InChIKey":
        print(d_row["descriptor"])
