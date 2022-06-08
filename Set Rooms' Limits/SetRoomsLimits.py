
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

TransactionManager.Instance.ForceCloseTransaction()

doc = DocumentManager.Instance.CurrentDBDocument
t = Transaction(doc, 'Set room limits')

rooms = UnwrapElement(IN[0])
projLevels = UnwrapElement(IN[1])
height = IN[2]/30.48

upperOfsetLevels = []
lastFloorRooms = []
enumRooms = []

lastLevel = projLevels[len(projLevels)-1]

for room in rooms:
	level = room.Level
	if level.Id == lastLevel.Id:
		lastFloorRooms.append(room)
	else:
		enumRooms.append(room)
		for projLevel in projLevels:
			if projLevel.Elevation - level.Elevation >= 6.5616:
				upperOfsetLevels.append(projLevel.Id)
				break

t.Start()

for i, room in enumerate(enumRooms):
	room.get_Parameter(BuiltInParameter.ROOM_UPPER_OFFSET).Set(height)
	room.get_Parameter(BuiltInParameter.ROOM_UPPER_LEVEL).Set(upperOfsetLevels[i])
	
if lastFloorRooms != []:
	for room in lastFloorRooms:
		room.get_Parameter(BuiltInParameter.ROOM_UPPER_OFFSET).Set(6.5616)

t.Commit()

OUT = rooms, lastFloorRooms
