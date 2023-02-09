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

clr.AddReference("RevitAPI")

import Autodesk
from Autodesk.Revit.DB import Curve

curves = UnwrapElement(IN[0])
outlist = []

for list in curves:
	intersectlist = []
	for i, curve0 in enumerate(list):
		intersectsublist = []
		for j, curve1 in enumerate(list):
			if curve0.Intersect(curve1):
				if i not in intersectsublist:
					intersectsublist.append(i)
				intersectsublist.append(j)
		if intersectsublist:
			test = True
			for l in intersectlist:
				if any(elem in l for elem in intersectsublist):
					l += intersectsublist
					test = False
					break
			if test:
				intersectlist.append(intersectsublist)			
	outlist.append(intersectlist)
				
OUT = outlist
