import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPI")

import Autodesk
from Autodesk.Revit.DB import Point, XYZ

outlist = []

minPoints = UnwrapElement(IN[0])
maxPoints = UnwrapElement(IN[1])

for i, list in enumerate(minPoints):
	sublist = []
	for j, pt in enumerate(list):
		templist = []
		ptAx = pt.X / 30.48
		ptAy = pt.Y / 30.48
		ptAz = pt.Z / 30.48
		ptB = maxPoints[i][j]
		ptBx = ptB.X / 30.48
		ptBy = ptB.Y / 30.48
		templist.append(pt)
		templist.append(Point.Create(XYZ(ptBx, ptAy, ptAz)).ToProtoType())
		templist.append(ptB)
		templist.append(Point.Create(XYZ(ptAx, ptBy, ptAz)).ToProtoType())
		sublist.append(templist)
	outlist.append(sublist)
	
OUT = outlist
