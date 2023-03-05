import sys
import os

sys.path.insert(0, "/net/users/chenghua/Python/Util/")
from Path.pathFinder import PathFinderFtpTree

def main():
	filepath_pdb_ids = 'structure_files/list'
	l_pdb_id = []
	with open(filepath_pdb_ids) as file:
		for line in file:
			l_pdb_id.append(line.split('.')[0].lower())

	for pdb_id in l_pdb_id:
		filepath=PathFinderFtpTree(pdb_id).GetPath("validation_cif")
		print(filepath)
		if filepath:
			os.system("cp %s %s" % (filepath, "validation_reports"))

if __name__ == "__main__":
    main()
