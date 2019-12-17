# Instagram_Squarify
A small python script to automate adding a blurred background to images to make them instagram compatible.

I frequently edit pictures I take on mobile/camera and edit them in Lightroom on PC and post on instagram. In this process I may sometimes need to use some third party apps to add background-blur etc. This whole process requires me to transfer images multiple times between devices and process them on different devices. So I decided to automate this step using python.  

Usage:
* Just paste the image files to be squarifed into pictures folder and run 'main.py' to run with default settings.

* If you want to manually adjust the background blur or brightness use '--blur_strength' or '--background_brightness' flags.
Example: 
    ```
    python main.py --blur_strength 100 --backgroung_brightness 1.3
    ```

### Before formatting
(5333 x 2995)
![picture alt](https://github.com/Pranay-modukuru/Instagram_Squarify/blob/master/pictures/icymountain.jpg "before formatting")

### After formatting
(1080 x 806)
![picture alt](https://github.com/Pranay-modukuru/Instagram_Squarify/blob/master/output_files/icymountain.jpg "after formatting")
