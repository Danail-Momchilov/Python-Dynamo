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

floorfaces = []

opt = Options()
opt.ComputeReferences = True

if isinstance(IN[0], list):
	floors = UnwrapElement(IN[0])
else:
	floors = [UnwrapElement(IN[0])]

for floor in floors:
	flSolid = GetElementSolids(floor, opt)[0]
	floorfaces.append(GetUppermostFace(flSolid).ToProtoType())

OUT = floorfaces
