"""Trajectory module
"""

import xdrfile


class Trajectory(xdrfile.XDRFile):
    """ changed Trajectory class to use new XDRFile class and keep old scripts working"""

    def __init__(self, filename, **kwargs):
        xdrfile.XDRFile.__init__(self, filename, **kwargs)

    def get_natoms(self):
        return self.natoms
