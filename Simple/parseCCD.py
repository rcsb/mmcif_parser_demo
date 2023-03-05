#!/usr/bin/env python3
# =============================================================================
# Author:  Chenghua Shao
# Date:    2023-02-17
# Updates:
# =============================================================================
"""
mmmcif parser demo CCD parsing
"""

from mmcif.io.IoAdapterCore import IoAdapterCore
# File IO class, read and write mmcif file


class CCD():
    """Class to process CCD file
    """

    def __init__(self):
        self.io = IoAdapterCore()

    def read(self, filepath_in):
        self.l_dc = self.io.readFile(filepath_in)
        self.dc0 = self.l_dc[0]

    def getStatus(self):
        pass
    
    def getDescriptor(self):
        descriptor = self.dc0.getObj('pdbx_chem_comp_descriptor')
        n_rows = descriptor.getRowCount()
        for i in range(n_rows):
            d_row = descriptor.getRowAttributeDict(i)
            if d_row["type"] == "InChIKey":
                print(d_row["descriptor"])

    def write(self, filepath_out):
        """
        Write the current data container list into a file

        Parameters
        ----------
        filepath_out : str
            output filepath.

        Returns
        -------
        None.

        """
        try:
            self.io.writeFile(filepath_out, self.l_dc)
        except IOError as e:
            pass
        


def main():
    filepath = "ligand_files/ATP.cif"
    ccd = CCD()
    ccd.read(filepath)
    ccd.getDescriptor()


if __name__ == "__main__":
    main()
