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

filepath = "structure_files/2hyv.cif"
io = IoAdapterCore()
list_data_container = io.readFile(filepath)
# read file, generate list of data containers

data_container = list_data_container[0]
# select the 1st data container

ligand = data_container.getObj('pdbx_entity_nonpoly')
# obtain data category from data container

n_rows = ligand.getRowCount()
# get number of data record rows

for i in range(n_rows):
    d_ligand = ligand.getRowAttributeDict(i)
    if d_ligand["name"] != "water":
        print("CCD id: %s; name: %s" %
              (d_ligand["comp_id"], d_ligand["name"]))
