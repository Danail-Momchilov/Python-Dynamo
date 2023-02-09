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

def compareListsSorted(list0, list1):
	doesContain = True
	sortLst = sorted(list1)
	for list in list0:
		if sorted(list) == sorted(sortLst):
			doesContain = False
	return doesContain

curves = UnwrapElement(IN[0])
outlist = []

for list in curves:
	intersectlist = []
	for i, curve0 in enumerate(list):
		intersectsublist = []
		for j, curve1 in enumerate(list):
			if i != j:
				if curve0.Intersect(curve1):
					if i not in intersectsublist:
						intersectsublist.append(i)
					intersectsublist.append(j)
		if intersectsublist:
			if compareListsSorted(intersectlist, intersectsublist):
				intersectlist.append(intersectsublist)
	outlist.append(intersectlist)
				
OUT = outlist
