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

# get detail items tags to use for the schemes
loadedTags = FilteredElementCollector(doc).OfClass(FamilySymbol)

tagsDict = {}
for elem in loadedTags:
	if elem.FamilyName in ["IPA-TAG-DI-Colector", "IPA-TAG-DI-Lira", "IPA-TAG-DI-Heatmeter", "IPA-TAG-DI-Panel radiator", "IPA-TAG-DI-Rad"]:
		tagsDict[elem.FamilyName] = elem.Id

TransactionManager.Instance.ForceCloseTransaction()




test = []




with Transaction(doc, "Update Detail Item's info") as t:
	t.Start()

	for i, item in enumerate(detItems):

		originalItem = modelElements[i]
		reference = Reference(item)
		tagOrientation = TagOrientation.Horizontal
		itemLocation = item.Location.Point
		
		if item.Symbol.FamilyName == "IPA-DI-Heatmeter":
			item.LookupParameter("Length").Set(modelElements[i].Symbol.LookupParameter("Length").AsDouble())
			item.LookupParameter("Conectors").Set(modelElements[i].Symbol.LookupParameter("Conectors").AsInteger())
			item.LookupParameter("Level_HC").Set(modelElements[i].LookupParameter("Entrance_HC").AsString())
			item.LookupParameter("Entrance_HC").Set(modelElements[i].LookupParameter("Entrance_HC").AsString())
			item.LookupParameter("Qheat").Set(modelElements[i].LookupParameter("Qheat").AsDouble())			
			tagTypeId = tagsDict["IPA-TAG-DI-Heatmeter"]			
			translation = XYZ(item.LookupParameter("Length").AsDouble()-1.5, 2.5, 0)
			
		elif item.Symbol.FamilyName == "IPA-DI-Colector":
			item.LookupParameter("Length").Set(modelElements[i].Symbol.LookupParameter("Length").AsDouble())
			item.LookupParameter("Conectors").Set(modelElements[i].Symbol.LookupParameter("Conectors").AsInteger())
			item.LookupParameter("Vis 2").Set(modelElements[i].Symbol.LookupParameter("Vis 2").AsInteger())
			item.LookupParameter("Vis Array").Set(modelElements[i].Symbol.LookupParameter("Vis Array").AsInteger())
			item.LookupParameter("Qheat").Set(modelElements[i].LookupParameter("Qheat").AsDouble())
			item.LookupParameter("Area_Number-HC").Set(modelElements[i].LookupParameter("Area_Number-HC").AsString())
			item.LookupParameter("Branches_HC").Set(modelElements[i].Symbol.LookupParameter("Branches_HC").AsString())
			item.LookupParameter("Main Branch").Set(modelElements[i].LookupParameter("Main Branch").AsDouble())
			tagTypeId = tagsDict["IPA-TAG-DI-Colector"]
			translation = XYZ(item.LookupParameter("Length").AsDouble() - 0.5, 3, 0)
			
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
			item.LookupParameter("Q_HC").Set(modelElements[i].LookupParameter("Q_HC").AsDouble())
			tagTypeId = tagsDict["IPA-TAG-DI-Lira"]
			translation = XYZ(item.LookupParameter("Width_HC").AsDouble() - 0.75, item.LookupParameter("Height_HC").AsDouble() + 1.5, 0)
			
		elif item.Symbol.FamilyName == "IPA-DI-Radiator":
			item.LookupParameter("Height_HC").Set(modelElements[i].Symbol.LookupParameter("Height_HC").AsDouble())
			item.LookupParameter("d").Set(modelElements[i].Symbol.LookupParameter("d").AsDouble())
			item.LookupParameter("N_glider").Set(modelElements[i].LookupParameter("N_glider").AsInteger())
			item.LookupParameter("Q_HC").Set(modelElements[i].LookupParameter("Q_HC").AsDouble())
			item.LookupParameter("Glider pcs.").Set(modelElements[i].LookupParameter("Glider pcs.").AsDouble())
			item.LookupParameter("H_Glider").Set(modelElements[i].Symbol.LookupParameter("H_Glider").AsDouble())
			for conn in originalItem.MEPModel.ConnectorManager.Connectors:
				if conn.Description == "HWS-Upper":
					if conn.MEPSystem:
						item.LookupParameter("termo ventil up").Set(1)
			tagTypeId = tagsDict["IPA-TAG-DI-Rad"]
			translation = XYZ(item.LookupParameter("Width_HC").AsDouble() - 0.9, item.LookupParameter("Height_HC").AsDouble() + 1.5, 0)
			test.append(item.LookupParameter("Height_HC"))
		
		elif item.Symbol.FamilyName == "IPA-DI-Panel Radiator":
			item.LookupParameter("Width_HC").Set(modelElements[i].LookupParameter("Length_HC").AsDouble())
			item.LookupParameter("Height_HC").Set(modelElements[i].Symbol.LookupParameter("Height_HC").AsDouble())
			item.LookupParameter("Q_HC").Set(modelElements[i].LookupParameter("Q_HC").AsDouble())
			tagTypeId = tagsDict["IPA-TAG-DI-Panel radiator"]
			translation = XYZ(item.LookupParameter("Width_HC").AsDouble() / 2, item.LookupParameter("Height_HC").AsDouble() + 1, 0)
			
		# tag the element
		tag = IndependentTag.Create(doc, doc.ActiveView.Id, reference, False, TagMode.TM_ADDBY_CATEGORY, tagOrientation, itemLocation)
		tag.ChangeTypeId(tagTypeId)
		tag.Location.Move(translation)
			
	t.Commit()

OUT = str(i) + " Detail Items' parameters were successfully updated in accordance with their original model elements!", test
