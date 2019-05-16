#this is my geometry analysis code
import numpy
import os
import sys #this is used to get variables from the command line

def calculate_distance(atom1,atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list #datatype we expect this to be
        A list of coordinates [x, y, z]
    atom2: list
        A list of coordinates [x, y, z]

    Returns
    -------
    distance: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0,0,0], [0,0,1])
    1.0
    """ #dot string to show when you go into the help doc of this function
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+ y_distance**2+z_distance**2)
    return distance

def bond_check(bond_distance,bond_min=0,bond_max=1.5): # we can define the default min and max in the def
    """
    Check to see if 'bond' is an actual bond between 2 atoms

    Parameters
    ----------
    bond_distance: float
        The distance calculated in calculate_distance between 2 atoms.
    bond_min: float
        The minimum distance accepted as a 'bond'. The default is 0.
    bond_max: float
        The maximum distance accepted as a 'bond'. The default is 1.5.

    Returns
    -------
    True: string
        Tells that the bond distance is within the range of the minimum and the maximum
    False: string
        Tells that the bond distance is out of the range of the minimum and the maximum

    Examples
    --------
    >>> bond_check(1.0)
    True

    >>> bond_check(1.5,bond_min=0,bond_max=1.0)
    False
    """
    if bond_distance >bond_min and bond_distance<bond_max:
        return True
    else:
        return False

if __name__ == "__main__":
    #lets us use this file as a script in python command line
    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file.')
        #error if a file was not given in the command line
    file_location = sys.argv[1]
#we use 1 because everything after python is and argument
#file location is considered input on the command line
    xyz_file=numpy.genfromtxt(fname=file_location,delimiter='',skip_header=2,dtype='unicode')
    symbols= xyz_file[:,0]
    coordinates = coordinates.astype(numpy.float)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB<numA:
                distance_AB = calculate_distance(atomA,atomB)
                if bond_check(distance_AB) == True:
                    print (F'{symbols[numA]} to {symbols[numB]} : {distance_AB:.3f}')
