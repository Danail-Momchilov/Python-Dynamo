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

opt = Options()

outlist1, outlist2 = [], []

floors = UnwrapElement(IN[0])

for floor in floors:
	templist = []
	solid = floor.get_Geometry(opt)
	for f in solid:
		faces = f.Faces
		for face in faces:
			try:
				if face.FaceNormal.Z == 1:
					outlist1.append(face)
					outlist2.append(face.GetEdgesAsCurveLoops())
			except:
				pass
	
OUT = outlist1, outlist2
