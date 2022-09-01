
import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)


doc = DocumentManager.Instance.CurrentDBDocument


elements = UnwrapElement(IN[0])
views = UnwrapElement(IN[1])

elementIds = []


for list in elements:
	templist = []
	for element in list:
		templist.append(element.Id)
	tempcol = List[ElementId](templist)
	elementIds.append(tempcol)


TransactionManager.Instance.EnsureInTransaction(doc)

for i, view in enumerate(views):
	view.UnhideElements(elementIds[i])
	
TransactionManager.Instance.TransactionTaskDone()


if IN[0] != []:
	OUT = "Specified Text Notes were successfully unhidden from all views!"
else:
	OUT = None
