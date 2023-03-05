#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo simplest example
"""

from mmcif.io.IoAdapterCore import IoAdapterCore 
#File IO class, read and write mmcif file

filepath = "structure_files/2hyv.cif"
io = IoAdapterCore()
list_data_container = io.readFile(filepath) 
# read file, generate list of data containers 

data_container = list_data_container[0] 
# select the 1st data container

entity = data_container.getObj('entity') 
# obtain entity data category from data container

print(entity.data)
# get all data

print(entity.getAttributeValueList("type")) 
# get list of values by attr

print(entity.getRowAttributeDict(0)) 
# get 1st data row as dictionary

print(entity.getValue("pdbx_description",0)) 
# get value of a data cell by attr and index
