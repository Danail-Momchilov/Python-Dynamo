APIIntersections

> this nodes works with three inputs: Revit floor elements and min and max points for bounding boxes

> points are obtained from bounding boxes geometry of selected linked elements

> it is using the API to extraxct each floor's uppermost face, build solids from the min and max points and detech intersections' geometry directly in the API

> it returns uppermost planar faces of all intersections found, as well as their corresponding floor faces

![image](https://user-images.githubusercontent.com/46314846/219318800-bbb1da43-f34a-4e44-aed9-ef54d4c08e5b.png)

IntersectSurfaces

> this nodes takes surfaces as an input and returnes indices of all openings that should be group

> those are usually surfaces, taht are either intersecting partially or completely (e.g in the second case one of them is completely within the other)

![image](https://user-images.githubusercontent.com/46314846/219321103-abb8ff49-7b50-4d13-a059-2938c95632c9.png)






