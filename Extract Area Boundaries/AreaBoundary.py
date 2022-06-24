import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

areas = UnwrapElement(IN[0])
curveslist = []

Options = SpatialElementBoundaryOptions()
Options.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Center

for area in areas:
	curvesSublist = []
	for curve in area.GetBoundarySegments(Options)[0]:
		curvesSublist.append(curve.GetCurve().ToProtoType())
	curveslist.append(curvesSublist)

OUT = curveslist
