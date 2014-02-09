"""
    test_get_publication.py -- Given a URI of an publication, return a python
    structure representing the attributes of the publication

    Version 0.1 MC 2013-12-27
    --  Initial version.

"""

__author__      = "Michael Conlon"
__copyright__   = "Copyright 2013, University of Florida"
__license__     = "BSD 3-Clause license"
__version__     = "0.1"

import vivotools as vt
from datetime import datetime

print datetime.now(),"Start"
publications = [
    "http://vivo.ufl.edu/individual/n4160403698",
    "http://vivo.ufl.edu/individual/n49408",
    "http://vivo.ufl.edu/individual/n5988333327",
    "http://vivo.ufl.edu/individual/n697590874",
    "http://vivo.ufl.edu/individual/n7170943995",
    "http://vivo.ufl.edu/individual/no-such-pub",
    "http://vivo.ufl.edu/individual/n536643140",
    "http://vivo.ufl.edu/individual/n5202165124",
    "http://vivo.ufl.edu/individual/n898775618",
    "http://vivo.ufl.edu/individual/n5755807043"
    ]
for publication in publications:
    print "\n",vt.get_publication(publication)
print datetime.now(),"Finish"
