### Maps2CleanJSON

Based on the wish to migrate Google Maps places to another Google account, I came accross some problems with exporting the Google Maps Takeout content. After following the guide from [Velizara Tellalyan, 2021](https://www.velizaratellalyan.com/content-marketing/how-to-add-a-list-of-saved-google-maps-places-to-a-website/#9_Import_the_KLM_File_as_a_New_Layer_to_your_Custom_Google_Map) on how to export Maps Takeout data, this guide was really helpful except Google might has changed their `json` structure. 

<a href="url"><img src="https://github.com/schomakers/Maps2CleanJSON/blob/main/assets/takeout_screenshot.png" align="center" width=450></a>

This Python script adapts the outputted structure. After transforming the json using `main.py`, the output file can be used in an e.g. online editor (at least that was my procedure following Velizara's guide) like this one: [https://mygeodata.cloud/](https://mygeodata.cloud/), last accessed 4th January 2026 and transform the file to `.kml`. This file can then be used as a base for [https://mymaps.google.com/](https://mymaps.google.com/).

<a href="url"><img src="https://github.com/schomakers/Maps2CleanJSON/blob/main/assets/mygeodata_cloud.png" align="center" width=450></a>


**Note**: To my knowledge individual set points, just like the 2nd exmaple entry land just somewhere close to the Gulf of Guinea (coordinates 0,0 are assigned). I'll research on how to overcome this issue.