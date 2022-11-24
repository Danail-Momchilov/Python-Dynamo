# imports
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


# input variables
detItems = UnwrapElement(IN[0])
modelElements = UnwrapElement(IN[1])


TransactionManager.Instance.ForceCloseTransaction()

with Transaction(doc, "Update Detail Item's info") as t:
	t.Start()

	for i, item in enumerate(detItems):

		originalItem = modelElements[i]
		
		if item.Symbol.FamilyName == "IPA-DI-Heatmeter":
			item.LookupParameter("Length").Set(modelElements[i].Symbol.LookupParameter("Length").AsDouble())
			item.LookupParameter("Conectors").Set(modelElements[i].Symbol.LookupParameter("Conectors").AsInteger())
			
		elif item.Symbol.FamilyName == "IPA-DI-Colector":
			item.LookupParameter("Length").Set(modelElements[i].Symbol.LookupParameter("Length").AsDouble())
			item.LookupParameter("Conectors").Set(modelElements[i].Symbol.LookupParameter("Conectors").AsInteger())
			item.LookupParameter("Vis 2").Set(modelElements[i].Symbol.LookupParameter("Vis 2").AsInteger())
			item.LookupParameter("Vis Array").Set(modelElements[i].Symbol.LookupParameter("Vis Array").AsInteger())
			
		elif item.Symbol.FamilyName == "IPA-DI-Lira":
			item.LookupParameter("Width_HC").Set(modelElements[i].Symbol.LookupParameter("Width_HC").AsDouble())
			item.LookupParameter("Height_HC").Set(modelElements[i].LookupParameter("Height_HC").AsDouble())
			item.LookupParameter("Height Element pcs. 2").Set(modelElements[i].LookupParameter("Height Element pcs. 2").AsDouble())
			item.LookupParameter("Height Element pcs. 3").Set(modelElements[i].LookupParameter("Height Element pcs. 3").AsDouble())
			item.LookupParameter("Height Element pcs. 4").Set(modelElements[i].LookupParameter("Height Element pcs. 4").AsDouble())
			item.LookupParameter("Height Element pcs. 5").Set(modelElements[i].LookupParameter("Height Element pcs. 5").AsDouble())
			item.LookupParameter("Element pcs. 1").Set(modelElements[i].LookupParameter("Element pcs. 1").AsInteger())
			item.LookupParameter("Element pcs. 2").Set(modelElements[i].LookupParameter("Element pcs. 2").AsInteger())
			item.LookupParameter("Element pcs. 3").Set(modelElements[i].LookupParameter("Element pcs. 3").AsInteger())
			item.LookupParameter("Element pcs. 4").Set(modelElements[i].LookupParameter("Element pcs. 4").AsInteger())
			item.LookupParameter("Element pcs. 5").Set(modelElements[i].LookupParameter("Element pcs. 5").AsInteger())
			
		elif item.Symbol.FamilyName == "IPA-DI-Radiator":
			item.LookupParameter("Height_HC").Set(modelElements[i].Symbol.LookupParameter("Height_HC").AsDouble())
			item.LookupParameter("d").Set(modelElements[i].Symbol.LookupParameter("d").AsDouble())
			item.LookupParameter("N_glider").Set(modelElements[i].LookupParameter("N_glider").AsInteger())
			for conn in originalItem.MEPModel.ConnectorManager.Connectors:
				if conn.Description == "HWS-Upper":
					if conn.MEPSystem:
						item.LookupParameter("termo ventil up").Set(1)
		
		elif item.Symbol.FamilyName == "IPA-DI-Panel Radiator":
			item.LookupParameter("Width_HC").Set(modelElements[i].LookupParameter("Length_HC").AsDouble())
			item.LookupParameter("Height_HC").Set(modelElements[i].Symbol.LookupParameter("Height_HC").AsDouble())			
			
	t.Commit()

OUT = str(i) + " Detail Items' parameters were successfully updated in accordance with their original model elements!"
