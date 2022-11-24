
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


# a definition to determine the number of heatmeters within a given Area
def numberOfCollectors(equipmentList):
	count = 0
	for equipment in equipmentList:
		if 'DANFOSS' in equipment.Symbol.FamilyName:
			count += 1
	return count


# a definition that splits a list in two, with the heatmeters in one list and all the rest of the equipment in another
def removeHeatmetersFromList(equipmentList):
	heatmeters, equipment = [], []
	for elem in equipmentList:
		if 'DANFOSS' in elem.Symbol.FamilyName:
			heatmeters.append(elem)
		else:
			equipment.append(elem)
	return heatmeters, equipment


# a definition, returning all of the system names, available within each element in a list 
def returnElementSystems(equipmentList):
	outlist = []
	for elem in equipmentList:
		templist = []
		for connector in elem.MEPModel.ConnectorManager.Connectors:
			try:
				templist.append(connector.MEPSystem.Name)
			except:
				pass
		outlist.append(templist)
	return outlist


# split areas, based on heatmeters
def splitAreas(heatmeters, equipment, heatmeterSystems, equipmentSystems):
	outlist = []
	for i, heatmeterS in enumerate(heatmeterSystems):
		newAreaList = []
		newAreaList.append(heatmeters[i])
		for j, equipmentS in enumerate(equipmentSystems):
			if any(x in equipmentS for x in heatmeterS):
				newAreaList.append(equipment[j])
		outlist.append(newAreaList)
	return outlist


# input and output variables
elements = UnwrapElement(IN[0])
returnList = []


# main
for entrance in elements:
	entranceList = []
	for level in entrance:
		levelList = []
		for area in level:
			if numberOfCollectors(area) > 1:
				heatmeters, equipment = removeHeatmetersFromList(area)
				heatmetersSystems = returnElementSystems(heatmeters)
				equipmentSystems = returnElementSystems(equipment)
				for list in splitAreas(heatmeters, equipment, heatmetersSystems, equipmentSystems):
					levelList.append(list)			
			else:
				levelList.append(area)
		entranceList.append(levelList)
	returnList.append(entranceList)


OUT = returnList
