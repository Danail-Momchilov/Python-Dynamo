BoolMaskSizes

> This node is used to group and filter structural openings, located at the same X and Y coordinates, but with a different Z component and also having identical sizes

![image](https://user-images.githubusercontent.com/46314846/170255404-f332b2a2-ed51-44b9-b515-3554161818d9.png)

> Being identified in this way, they can all get the ID of the 'parent' element (typically the one, located at the lowest point), written in a locked parameter

> Once done, all elements can be automatically updated, according to the new location and size of the 'parent'


IdentifyPartnerChanges

> This node takes as arguments 'partnering' openings and their original ones

> It checks wether or not any changes were made to the groups of elements and filters only those with changed position and / or sizes

![image](https://user-images.githubusercontent.com/46314846/184125392-8999238e-6723-4058-948e-da03f192edfb.png)

> in the following example, only the group on the left will remain for correction

![image](https://user-images.githubusercontent.com/46314846/184125802-50336896-3dcf-40dd-bfd1-8bbdfb4fda73.png)

> this simple operation optimises performance significantly for large - scale projects, when thousands of elements need to be aligned
