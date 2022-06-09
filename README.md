Photo Editing Software   Version 1.3   02/25/2021


Description
------------ 
This is a photo-editing program that will allow filters to be applied on any user 
selected image, allowing one to implement filters and a curve-drawing tool on any 
selected image with the use of an interactive text-based interface or a batch user 
interface. 


Installation
-------------
To install this project several libraries must be downloaded and saved in the directory 
that you wish to run these programs in. These libraries include Cimpl.py, simple_Cimpl_filters.py, 
point_manipulation.py which can be obtained on the Cu-Learn webpage. In addition both the newest 
versions of Python pip (May already be installed on the newest versions of Python) and Numpy. 
These public libraries are directly installed from the WIndows Command Center or the Mac Control Center. 
To install pip on Windows use the command line >> py get-pip.py, for Mac use >> python get-pip.py. 
For numpy on either operating system use >> pip install numpy. Note that numpy requires pip to be 
installed beforehand.


Usage
------
Interactive ui usage:

- Typing “L” will allow the user to load an image
- Typing “S” will allow the user to save the edited image
- Typing “Q” will quit the program
- Typing “3” will apply the 3-tone filter 
- Typing “E” will apply the Edge detection filter
- Typing “D” will apply the Draw curve filter
- Typing “X” will apply the Extreme contrast filter
- Typing “T” will apply the Tint sepia filter
- Typing “P” will apply the Posterize filter
- Typing “V” will apply the Vertical flip filter
- Typing “H” will apply the Horizontal flip filter

Note that these user inputs are not case sensitive. For all letters both lower and upper 
case are valid inputs.


Credits
--------
Khalifeh Basiri: blue_channel / sepia / flip_vertical / interactive_ui
Arun Ichsanow: green_channel / combine / three_tone / draw_curve / batch_ui
Jason Perrins: red_channel / extreme_contrast / flip_horizontal / interactive_ui
Ephraim Inyang: posterize / detect_edges / batch_ui


Photo Editing Software can be reached at:

Voice: 613-413-9403
E-mail: khalifabasiri@cmail.carleton.ca



License
--------
Copyright (c) [2021] [Khalifeh Basiri, Arun Ichsanow, Jason Perrins, Ephraim Inyang]

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the Photo Editing Software), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons 
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
