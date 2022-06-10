> this script takes rooms, levels and a specified negative number as inputs

![image](https://user-images.githubusercontent.com/46314846/173022321-9580f722-8349-4b94-b4ab-d6a5fa518618.png)

> this is how rooms were initially set in the example

![image](https://user-images.githubusercontent.com/46314846/173022815-2240e7a5-f8fd-46db-900e-9b9f9dcd141d.png)

> for each one, the script takes its Level, finds the nearest one above, located at a distance larger than 200cm and sets it as an Upper Limit. Afterwards, it sets the Limit Offset, based on the specified input

![image](https://user-images.githubusercontent.com/46314846/173023477-eafdbf44-a3fa-4263-9bbc-391b3b9dff7a.png)

> if any room is found to be located on the uppermost floor, its Upper Limit will be set to the associated level and the Limit Offset will be set to 200cm
