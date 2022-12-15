import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import System
from System import Array
from System.Collections.Generic import *
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

from itertools import islice

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

outlistStart = []
outlistCenter = []

for n, list in enumerate(IN[0]):
	centerPts = list
	centerPtsFixed = list
	startPts = IN[1][n]
	startPtsFixed = startPts
	zCoords = IN[2][n]
	sum = zCoords.Count
	if centerPts.Count == sum:
		pass
	else:
		dif = sum - centerPts.Count
		i = int(centerPts.Count)
		lastCenterPt = centerPts[i-1]
		lastStartPt = startPts[i-1]
		while (i < sum):
			pointCenterXYZ = XYZ(lastCenterPt.X / 304.8, lastCenterPt.Y / 304.8, zCoords[i] / 304.8)
			pointStartXYZ = XYZ(lastStartPt.X / 304.8, lastStartPt.Y / 304.8, zCoords[i] / 304.8)
			newCenterPoint = Point.Create(pointCenterXYZ).ToProtoType()
			newStartPoint = Point.Create(pointStartXYZ).ToProtoType()
			centerPtsFixed.append(newCenterPoint)
			startPtsFixed.append(newStartPoint)
			i += 1
		outlistCenter.append(centerPtsFixed)
		outlistStart.append(startPtsFixed)
		
OUT = outlistStart, outlistCenter
