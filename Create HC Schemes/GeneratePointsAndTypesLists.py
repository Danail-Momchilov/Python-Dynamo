
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *


x, y, i = 0, 0, 0
xList, yList = [], []
types, ids = [], []


detItemTypes = IN[1]

def getDetItemType(famName, itemsList):
	if "DANFOSS" in famName:
		return(itemsList[0])
	elif "ME-Radiator" in famName:
		return(itemsList[4])
	elif "Lira" in famName:
		return(itemsList[2])
	elif "Heatmeter" in famName:
		return(itemsList[1])
	elif "Panel Radiator" in famName:
		return(itemsList[3])
	else:
		return(itemsList[3])


for entrance in UnwrapElement(IN[0]):

	x += 60000
	y = 0
	i = x
	
	for level in entrance:
	
		x = i	
		y += 2500
		j = 0
		
		
		if len(level[j]) == 1 and isinstance(level[j][0], FamilyInstance):
			xList.append(x)
			yList.append(y)
			types.append(getDetItemType(level[j][0].Symbol.FamilyName, detItemTypes))
			ids.append(level[j][0].Id)
			j += 1
			
		elif len(level[j][0]) == 0:
			j += 1
			
		if len(level) > 1 or j == 0:
			for apartment in level[j]:
				x -= 3000
				for l, elem in enumerate(apartment):
					xList.append(x)
					yList.append(y)
					if l != len(apartment) - 1:
						x = x - (apartment[l+1].LookupParameter("WidthReport").AsDouble())*300.48 - 800
					types.append(getDetItemType(elem.Symbol.FamilyName, detItemTypes))
					ids.append(elem.Id)
				
		x = i
		j += 1
		
		
		if len(level) == j + 1:
			for apartment in level[j]:
				x += 3000
				for k, elem in enumerate(apartment):
					xList.append(x)
					yList.append(y)
					x = x + (elem.LookupParameter("WidthReport").AsDouble())*300.48 + 800
					types.append(getDetItemType(elem.Symbol.FamilyName, detItemTypes))
					ids.append(elem.Id)


OUT = xList, yList, types, ids
