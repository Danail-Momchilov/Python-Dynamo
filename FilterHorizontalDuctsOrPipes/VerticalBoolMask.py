# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

outlist = []

for angle in IN[0]:
	if (angle <= 15 and angle != None):
		outlist.append(False)
	else:
		outlist.append(True)

OUT = outlist
