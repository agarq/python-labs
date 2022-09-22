#A package is simply a collection of modules. 
# It's a collection of related Python files all bundled up into single package.
# files must be in a folder and also is required to add the __init__.py file in blank 
# to tell Python, Hey, this is a package, not just a random collection of Python files in a folder.

from numbers.factors import getFactors 


print(getFactors(100))