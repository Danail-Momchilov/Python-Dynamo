
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import Point, Line, XYZ, CurveLoop, GeometryCreationUtilities, Options, BooleanOperationsUtils, BooleanOperationsType, PlanarFace, UV, BuiltInParameter, Reference

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

def GetElementSolids(element, opt):
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

def GetUppermostFace(solid):
	faces = []
	for face in solid.Faces:
		pt = UV(0.5, 0.5)
		normal = face.ComputeNormal(pt)
		if normal.Z == 1:
			faces.append(face)
	if faces.Count == 1:
		return faces[0]
	else:
		return faces

intersectFaces, floorSolids, bboxSolids, floorFaces, solidHeights = [], [], [], [], []

opt = Options()
opt.ComputeReferences = True

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
	templist = []	
	flSolid = GetElementSolids(floor, opt)[0]
	floorSolids.append(flSolid)
	floorFaces.append(GetUppermostFace(flSolid))
	solidHeights.append(round(floor.get_Parameter(BuiltInParameter.STRUCTURAL_FLOOR_CORE_THICKNESS).AsDouble()*30.48, 2))
	
for flSolid in floorSolids:
	templist = []
	for bbSolid in bboxSolids:
		intersect = [BooleanOperationsUtils.ExecuteBooleanOperation(flSolid, bbSolid, BooleanOperationsType.Intersect)][0]
		if intersect.Volume > 0:
			templist.append(GetUppermostFace(intersect).ToProtoType())
	intersectFaces.append(templist)

OUT = floorFaces, intersectFaces, solidHeights

