> this script represents the correct way of getting Revit solids from a room, so that they can be used in Dynamo later on

> rooms' solids could easily be obtained from the rooms' property .ClosedShell. However, by doing so, what you get is an Autodesk.Revit.DB.Solid, which cannot be wrapped back to dynamo solid. if you attempt to do so by using the .ClosedShell.ToProtoType() method, you get an error:

![image](https://user-images.githubusercontent.com/46314846/196372940-87ddec96-a586-4c7f-b123-cbdcf76a2c7a.png)

> however, if you get them through the SpatialElementGeometryCalculator(), wrapping works for both solids and their faces:

![image](https://user-images.githubusercontent.com/46314846/196373307-a04b4ad6-a545-452e-be54-02fdfcd7d5d4.png)

