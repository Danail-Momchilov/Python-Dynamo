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

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

rooms = UnwrapElement(IN[0])
outlist = []

options = SpatialElementBoundaryOptions()
options.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Finish
calculator = SpatialElementGeometryCalculator(doc)

for room in rooms:
	solid = calculator.CalculateSpatialElementGeometry(room).GetGeometry()
	
	for face in solid.Faces:
		outlist.append(face.ToProtoType())

OUT = outlist
