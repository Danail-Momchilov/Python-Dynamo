#Created by Danail Momchilov

import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FamilyInstance, Parameter, LocationPoint

def locationX(x):
	return x.Location.Point.X
	
def locationY(x):
	return x.Location.Point.Y

outlist = []
locationlist = []

mainlist = UnwrapElement(IN[0])
partnerslist = UnwrapElement(IN[1])

for i, elem in enumerate(mainlist):

	width = elem.LookupParameter('Element Opening Width').AsValueString()
	depth = elem.LookupParameter('Element Opening Depth').AsValueString()
	elemX = locationX(elem)
	elemY = locationY(elem)
	
	templist = []
	
	for partner in partnerslist[i]:
	
		partnerX = locationX(partner)
		partnerY = locationY(partner)
		partnerwidth = partner.LookupParameter('Element Opening Width').AsValueString()
		partnerdepth = partner.LookupParameter('Element Opening Depth').AsValueString()
		
		if partnerwidth == width and partnerdepth == depth and elemX == partnerX and elemY == partnerY and partner.Id != elem.Id:
			templist.append(True)
		else:
			templist.append(False)
			
	outlist.append(templist)
	
OUT = outlist
