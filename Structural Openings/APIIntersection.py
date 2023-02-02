import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import Point, Line, XYZ, CurveLoop, GeometryCreationUtilities, Options, BooleanOperationsUtils, BooleanOperationsType

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

def GetElementSolids(element,opt):
    elemSlds = []
    for geoEle in element.get_Geometry(opt):
        if geoEle.__class__ == Autodesk.Revit.DB.GeometryInstance:
            geoSet = geoEle.GetInstanceGeometry()
        else:
        	geoSet = [geoEle]
        for geoObj in geoSet:
            if geoObj.__class__ == Autodesk.Revit.DB.Solid:
                if geoObj.Volume > 0: elemSlds.append(geoObj)
    return elemSlds

outlist, floorSolids, bboxSolids = [], [], []

opt = Options()

minPts = UnwrapElement(IN[0])
maxPts = UnwrapElement(IN[1])
floors = UnwrapElement(IN[2])

for i, minPt in enumerate(minPts):
	maxPt = maxPts[i]
	pt0 = XYZ(minPt.X/30.48, minPt.Y/30.48, minPt.Z/30.48)
	pt1 = XYZ(maxPt.X/30.48, minPt.Y/30.48, minPt.Z/30.48)
	pt2 = XYZ(maxPt.X/30.48, maxPt.Y/30.48, minPt.Z/30.48)
	pt3 = XYZ(minPt.X/30.48, maxPt.Y/30.48, minPt.Z/30.48)
	edge0 = Line.CreateBound(pt0, pt1)
	edge1 = Line.CreateBound(pt1, pt2)
	edge2 = Line.CreateBound(pt2, pt3)
	edge3 = Line.CreateBound(pt3, pt0)
	edges = []
	edges.Add(edge0)
	edges.Add(edge1)
	edges.Add(edge2)
	edges.Add(edge3)
	height = maxPt.Z/30.48 - minPt.Z/30.48
	crvLoop = CurveLoop.Create(edges)
	loopList = []
	loopList.Add(crvLoop)
	bboxSolids.Add(GeometryCreationUtilities.CreateExtrusionGeometry(loopList, XYZ.BasisZ, height))
	
for floor in floors:
	floorSolids.append(GetElementSolids(floor, opt)[0])
	
intersectionSet = ( [ [ BooleanOperationsUtils.ExecuteBooleanOperation(s1, s2, BooleanOperationsType.Intersect) for s1 in floorSolids ] for s2 in bboxSolids ] )

for list in intersectionSet:
	templist = []
	for solid in list:
		if solid.Volume > 0:
			try:
				templist.append(solid.ToProtoType())
			except:
				pass
	outlist.append(templist)

OUT = outlist
