## Adapter = File; data container = data block; data category/object =  cif category

from mmcif.io.IoAdapterCore import IoAdapterCore #File IO class, read and write file to and from data containers
## the above adapter subsequently import the following 
## from mmcif.api.PdbxContainers import DataContainer #Data container class, at data block level, operate on categories such as add/remove
## from mmcif.api.DataCategory import DataCategory #Data Category class, at cif category level, operate on attributes and values
from mmcif.api.DataCategory import DataCategory #need to explicitly import if creating new cif category

##########################################################################################
##---File IO adater usage ---
io = IoAdapterCore()
filepath_in = "3sch.cif"
l_data_container = io.readFile(filepath_in) #generate list of data_container from file, 
l_data_container_selected = io.readFile(filepath_in,  selectList=['database_2']) #load selected cateogries only
io.writeFile("test_output.cif", l_data_container) #write data_container into a new file

l_data_container_selected = l_data_container[0:1] #select data container, remove others
io.writeFile("test_output.cif", l_data_container_selected) #write selected data_container into a new file

data_container = l_data_container[0] #select the 1st data_container

##########################################################################################
##---Data Container on Data Block usage ---
print(data_container.getObjNameList()) #get list of all categories
## print(data_container.getObjCatalog()) #get dictionary of the entire data_container, with key of category name
database_3 = DataCategory("database_3",attributeNameList=["test1","test2"],rowList=[["1","2"],["3","4"]]) #see Data category below
data_container.append(database_3) #add data category to data container
data_container.remove(database_3) #rempve category DOES NOT work
database_3.data = [] #essentially remove category when write the file out. 

database_2 = data_container.getObj('database_2') #read one data category from data container

##########################################################################################
##---Data Category Object on Cif Category usage ---
## each category can be viewed as dataframe with columns as attributes and data as rows
##---Whole-category read operation
print(database_2)
print(database_2.getAttributeList()) #get list of attributes
print(database_2.data) #get list of values, each element of the list is a list of values corresponding to the attributes
## [['PDB', 'test', '?'], ['RCSB', 'RCSB066034', '?'], ['WWPDB', 'D_1000066034', '?']]
## database_2.data = [] #essentially remove category when write the file out.

##--- get number of indices, can be used for enumerating the category
print(database_2.getRowCount()) #get num of rows, length of self.data

##--- read attributes
print(database_2.getAttributeValueList("database_id")) #get list of values by attr

##--- read index based on value
print(database_2.selectIndices("3SCH","database_code")) #get list of indices by pair of value and attr
print(database_2.selectIndicesFromList(["PDB","3SCH"],["database_id","database_code"])) #get list of indices by pair of value list and attr list

##--- read value based on index
print(database_2.getValue("database_id",0)) #get value of a data cell by attr and index
print(database_2.getRowAttributeDict(0)) #get dictionary of a row by index, with key of attr(without category name)

##--- update value based on attribute and index
database_2.setValue("test", attributeName="database_code", rowIndex=0) #set value for a cell by attr and index
##--- append new value row
index_appended_row = len(database_2.data)
database_2.setValue("database_added", "database_id",  index_appended_row)
database_2.setValue("code_added", "database_code", index_appended_row)

##--- update value based on attribute and current value
database_2.replaceValue("3SCH", "test","database_code") #replace value based on attr and current value
database_2.replaceSubstring("3SC", "test","database_code") #replace value substring based on attr and current value

##--- append new attribute
## database_2.appendAttribute("database_test1") #add new attribute without value
database_2.appendAttributeExtendRows("database_test2", defaultValue="?") #add new attr/item into the category

##--- create a new data/cif category
database_4 = DataCategory("database_4",attributeNameList=["test1","test2"],rowList=[["1","2"],["3","4"]])
## database_4 = DataCategory("database_4")
## database_4.appendAttribute("test3")
## database_4.appendAttribute("test4")
## database_4.append(["5","6"])
## database_4.append(["7","8"])
data_container.append(database_4)

##########################################################################################
print(io.writeFile("test_output.cif", l_data_container))




## print()
## print(database_2.getRowIndex()) #get current row index
## print(database_2.getFullRow(0)) #get a row in the form of list of the ordered values
## print(database_2.getAttributeListWithOrder()) #get a list of tuples, each tuple is attr and attr index
## print(database_2.getValueOrDefault("database_id",0)) #get value of a data cell, handle exception of error by default
## print(database_2.getRowItemDict(0)) #get dictionary of a row, note that the key is full cif item with underscore, e.g. _database_2.database_id
## print(database_2.getAttributeUniqueValueList("database_id"))
