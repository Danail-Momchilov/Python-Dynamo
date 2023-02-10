import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

import System
from System import Array

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
from Autodesk.Revit.DB import XYZ, Point, FamilySymbol
from Autodesk.Revit.Creation import Document

def cm(a):
	return a/30.48

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument

familySymbol = UnwrapElement(IN[1])
refVector = XYZ(1, 0, 0)
outlist = []

TransactionManager.Instance.EnsureInTransaction(doc)

for i, plFace in enumerate(IN[0]):
	for j, pt in enumerate(UnwrapElement(IN[2][i])):
		width = cm(IN[3][i][j])
		depth = cm(IN[4][i][j])
		height = cm(IN[5][i])
		ptXYZ = XYZ(cm(pt.X), cm(pt.Y), cm(pt.Z))
		instance = uidoc.Document.Create.NewFamilyInstance(plFace, ptXYZ, refVector,  familySymbol)
		instance.LookupParameter("Element Opening Width").Set(width)
		instance.LookupParameter("Element Opening Depth").Set(depth)
		instance.LookupParameter("Element Opening Height").Set(height)
		outlist.append(instance)
		
TransactionManager.Instance.TransactionTaskDone()

OUT = outlist
