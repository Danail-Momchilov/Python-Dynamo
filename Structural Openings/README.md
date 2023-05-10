APIIntersections

> this nodes works with three inputs: Revit floor elements and min and max points for bounding boxes

> points are obtained from bounding boxes geometry of selected linked elements

> it is using the API to extraxct each floor's uppermost face, build solids from the min and max points and detect intersections' geometry directly in the API

> it returns uppermost planar faces of all intersections found, as well as their corresponding floor faces

![image](https://user-images.githubusercontent.com/46314846/219318800-bbb1da43-f34a-4e44-aed9-ef54d4c08e5b.png)

IntersectSurfaces

> this node takes surfaces as an input and returnes indices of all openings that should be grouped

> those are usually surfaces, that are either intersecting partially or completely (e.g in the second case one of them is completely within the other)

![image](https://user-images.githubusercontent.com/46314846/219321103-abb8ff49-7b50-4d13-a059-2938c95632c9.png)

PlaceOpenings

> this node is simply placing structural opening families, based on its inputs: floors' planar faces, openings location points, sizes and thickness

> the final result is all openings, placed in the model correctly and most importantly, quickly, due to the operation being done completely in the API

![image](https://user-images.githubusercontent.com/46314846/219324252-f250ed2f-9a99-4b27-801f-c1f71fb221fa.png)

Overview

> these lines of code were inspired by the numerous problems, encountered by working with the same workflow, but done entirely in Dynamo

> it was quite often that the graph was failing, due to problems with geometry conversion, other than that it was extremely slow and time consiming

> after introducing those Python scripts, it works without making any mistakes and also extremely fast. Identical operation that used to take up to 10 minutes with the Dynamo graph, now takes around 8 seconds for all tasks to be completed in the API

![image](https://user-images.githubusercontent.com/46314846/219325311-73fbdeca-9c7c-4483-a723-41d0f222f625.png)







