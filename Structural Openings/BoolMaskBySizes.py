#Created by Danail Momchilov

import sys
import math
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FamilyInstance, Parameter, LocationPoint

def locationX(x):
	return round(x.Location.Point.X, 0)
	
def locationY(x):
	return round(x.Location.Point.Y, 0)

outlist = []

mainlist = UnwrapElement(IN[0])
partnerslist = UnwrapElement(IN[1])

for i, elem in enumerate(mainlist):

	width = elem.LookupParameter('Element Opening Width').AsDouble()*30.48
	depth = elem.LookupParameter('Element Opening Depth').AsDouble()*30.48
	elemX = locationX(elem)
	elemY = locationY(elem)
	
	templist = []
	
	for partner in partnerslist[i]:
	
		partnerX = locationX(partner)
		partnerY = locationY(partner)
		partnerwidth = partner.LookupParameter('Element Opening Width').AsDouble()*30.48
		partnerdepth = partner.LookupParameter('Element Opening Depth').AsDouble()*30.48
		difW = abs(partnerwidth - width)
		difD = abs(partnerdepth - depth)
		
		if difW <= 1.5 and difD <= 1.5 and elemX == partnerX and elemY == partnerY and elem.Id != partner.Id:
			templist.append(True)
		else:
			templist.append(False)
			
	outlist.append(templist)
	
OUT = outlist
