
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
	
def ElementWidth(x):
	return x.LookupParameter("Element Opening Width").AsDouble()*30.48
	
def ElementDepth(x):
	return x.LookupParameter("Element Opening Depth").AsDouble()*30.48


partnersOp = UnwrapElement(IN[0])
mainOp = UnwrapElement(IN[1])

outlistPartners = []
outlistMain = []
outlistWidth = []
outlistDepth = []

testlist = []


for i, opening in enumerate(mainOp):

	templist = []
	
	locX = locationX(opening)
	locY = locationY(opening)
	Width = ElementWidth(opening)
	Depth = ElementWidth(opening)
	
	for partner in partnersOp[i]:
	
		PlocX = locationX(partner)
		PlocY = locationY(partner)
		PWidth = ElementWidth(partner)
		PDepth = ElementDepth(partner)
		
		difW = abs(PWidth - Width)
		difD = abs(PDepth - Depth)
		
		if difW >= 1.5 or difD >= 1.5 or PlocX != locX or PlocY != locY: #and opening.Id != partner.Id:
			templist.append(partner)
			if opening not in outlistMain:
				outlistMain.append(opening)
				outlistWidth.append(Width)
				outlistDepth.append(Depth)
	
	if templist != []:
		outlistPartners.append(templist)


OUT = outlistPartners, outlistMain, outlistWidth, outlistDepth, testlist
