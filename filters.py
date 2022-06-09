from Cimpl import *
from simple_Cimpl_filters import grayscale
from point_manipulation import *
import numpy as np
import numpy.polynomial.polynomial as poly

# red_channel-------------------------------------------------------------------------------------------------------------------------
def red_channel(image: Image) -> Image: # applies the red channel
	""" Author: Jason Perrins
    
	Returns a copy of an image with the red channel.
    
	>>> image = load_image(choose_file())
	>>> new_image = red_channel(image)
	>>> show(new_image)
	"""
	new_image = copy(image)  # Creates a copy of an image
	for x, y, (r, g, b) in image: # loops through every pixel in the given image
		red = create_color(r, 0, 0)  # sets values for g and b to 0.
		set_color(new_image, x, y, red) # applies red color to a pixel for each
                                    	#itteration of the loop
	return new_image # returns a new image with the applied red filter

# green_channel----------------------------------------------------------------------------------------------------------------------
def green_channel(image: Image) -> Image: #applies the green filter
	""" Author: Arun Ichsanow
	Returns a green channel copy of an image.
	
	>>> image = load_image(choose_file())
        >>> new_image = green_channel(image)
        >>> show(new_image)
        """
	new_image = copy(image) # Creates a copy of the input image
	for x, y, (r, g, b) in image: # loops for every pixel in the image
		green = create_color(r - g, g, b - g) # decreases the red and blue value
		                                      # of the colour by the value of
		                                      # the value of the green component
		                                      # to create a green layer efect
		                                      # where the presence of red and
		                                      # blue determine the brigtness						      
		set_color(new_image, x, y, green) # applies the previously determined 
                                          # shade of green to the current pixel
	return new_image # returns the new image with the green layer

# blue_channel----------------------------------------------------------------------------------------------------------------------
def blue_channel(image: Image) -> Image:
	""" Author: khalifeh basiri
        Return a bluescale copy of image.
   
        >>> image = load_image(choose_file())
        >>> blue_image = blue_channel(image)
        >>> show(blue_image)
        """
	new_image = copy(image)
	for x, y, (r, g, b) in image:
		blue = create_color(0,0,b)
		set_color(new_image, x, y, blue)      
	return new_image

# combine----------------------------------------------------------------------------------------------------------------------
def combine(red_photo:Image, green_photo:Image, blue_photo:Image)-> Image:
	"""Author: Arun Ichsanow
	Combines the (r, g, b) pictures of a photo to produce a full colour photo.
	>>> combined('red_image', 'green_image', 'blue_image')
	Returns image of combined images """
	red_layer = copy(red_photo) # creates a copy of the red image
	green_layer = copy(green_photo) # creates a copy of the green image
	blue_layer = copy(blue_photo) # creates a copy of the blue image
	new_photo = red_layer # starts combining the rgb values by taking red as abase
	for pixel in green_layer: # loops for each pixel
		x, y, (r, g, b) = pixel # creates variables for each rgv value in each pixel
		r1, g1, b1 = get_color(new_photo, x, y) # takes the rgb from the blue layer
		set_color(new_photo, x, y, create_color(r1, g, b1)) # combines the combines the rgb values
	for pixel in blue_layer: # loops for each pixel
		x, y, (r, g, b) = pixel # creates variables for each rgv value in each pixel
		r1, g1, b1 = get_color(new_photo, x, y) # takes the rgb from the green layer
		set_color(new_photo, x, y, create_color(r1, g1, b))# combines the combines the rgb value
	return new_photo # returns combined image


# three_tone----------------------------------------------------------------------------------------------------------------------
def three_tone(image: Image, col1: str, col2: str, col3: str) -> Image:
	"""
	Author: Arun Ichsanow
	"""
	black = create_color(0,0,0)
	white = create_color(255,255,255)
	blood = create_color(255,0,0)
	green = create_color(0,255,0)
	blue = create_color(0,0,255)
	lemon = create_color(255,255,0)
	cyan = create_color(0,255,255)
	magenta = create_color(255,0,255)
	gray = create_color(128,128,128)
	colours_input = [col1, col2, col3]
	colours_possible_input = ["black", "white", "blood", "green", "blue", 
		                          "lemon", "cyan", "magenta", "gray"]
	colours_rgb = [black, white, blood, green, blue, lemon, cyan, 
		           magenta, gray]
	tones = [(),(),()]
	for i in range(3):
		for j in range(9):
			if colours_input[i] == colours_possible_input[j]:
				tones[i] = colours_rgb[j]
	
	new_image = copy(image)
	for x, y, (r, g, b) in image:
		if (r + g + b) // 3 < 85:
			set_color(new_image, x, y, tones[0])
		elif (r + g + b) // 3 < 171:
			set_color(new_image, x, y, tones[1])
		else:
			set_color(new_image, x, y, tones[2])
	return new_image

# extreme_contrast----------------------------------------------------------------------------------------------------------------------
def extreme_contrast(image: Image) -> Image:
	"""
	Author: Jason Perrins
	"""
	
	new_image = copy(image) # Creates a copy of an image
	for x, y, (r, g, b) in image: # loops through every pixel in the given image
		red_min = create_color(0, g, b)  # sets red pixel value to 0.
		red_max = create_color(255, g, b)  # sets red pixel value to 255.
		green_min = create_color(r, 0, b)  # sets green pixel value to 0.
		green_max = create_color(r, 255, b)  #sets green pixel value to 255.
		blue_min = create_color(r, g, 0)  # sets blue pixel value to 0.
		blue_max = create_color(r, g, 255)  # sets blue pixel value to 255.
		
		
		if r < 128 :
			set_color(new_image, x, y, red_min)
		else:
			set_color(new_image, x, y, red_max)
		if g < 128 :
			set_color(new_image, x, y, green_min)
		else:
			set_color(new_image, x, y, green_max)
		if b < 128 :
			set_color(new_image, x, y, blue_min)
		else:
			set_color(new_image, x, y, blue_max)  
			  
	return new_image

# sepia ----------------------------------------------------------------------------------------------------------------------
def sepia(image: Image) -> Image:
	"""AUTHOR: Khalifeh basiri
	Returns a tinted copy of the image.
	
	>>> image = load_image(choose_file())
	>>> tint_image = sepia(image)
	>>> show(tint_image)
	"""
	new_image = copy(image)  # Creates a copy of an image
	gray_image = grayscale(new_image) # applies grayscale dunction to the image
	for x, y, (r, g, b) in gray_image:# loops through every pixel in the given image
		if r < 63:
			tint = create_color(r * 1.1, g, b * 0.9)
		elif r < 192:
			tint = create_color(r * 1.15, g, b * 0.85)
		else:
			tint = create_color(r * 1.08, g, b * 0.93)
		set_color(gray_image, x, y, tint) # sets new colors to the image based on the rgb values.
	return gray_image # returns a new image with the applied sepia filter

# posterize; _adjust_component----------------------------------------------------------------------------------------------------------------------
def _adjust_component(value : int) -> int:
	"""
	Author: Ephraim Inyang
	"""
    
	midpoint = 0
    
	# Checks which quadrant the color is in and then sets a midpoint
    
	if value < 64 : 
    
		midpoint = 31
    
	elif value < 128 : 
    
		midpoint = 95
    
	elif value < 192 :
    
		midpoint = 159
    
	elif value < 256 :
    
		midpoint = 223
	    
	return midpoint

# posterize----------------------------------------------------------------------------------------------------------------------
def posterize(image : Image) -> Image :

	""" Author: Ephraim Inyang
	will return a posterized image
	"""
    
	new_image = copy(image) 
    
    
    
	for x,y, (r,g,b) in new_image:
    
		# Gets the midpoint of the color of the pixels
	
		r_midpoint = _adjust_component(r) 
	
		g_midpoint = _adjust_component(g)
	
		b_midpoint = _adjust_component(b)
	
	
	
		new_color = create_color(r_midpoint, g_midpoint, b_midpoint)
	
		set_color(new_image, x, y, new_color)
    
	return new_image

# detect_edges----------------------------------------------------------------------------------------------------------------------
def detect_edges(image:Image, threshold:int)->Image:
	"""
	Author: Ephraim Inyang
	Student Number: 101146896
    
	Returns a copy of an image after finding edges within the image.
	
	detect_edges
	"""
	new_image = copy(image)
	black = create_color(0, 0, 0)
	white = create_color(255, 255, 255)
	btm_pixel = get_height(new_image) 
	
	for x, y, pixel in new_image:
		nxt = y + 1 # Would have to add 1 to see the pixel below
		if y != (btm_pixel - 1): # Must -1 because it begins count from 0
			(r, g, b) = pixel
			top_brightness = (r + g + b) // 3 # calculating the brightness of the pixel on top
	    
			next_pixel = get_color(new_image, x, nxt)
			(btm_r, btm_g, btm_b) = next_pixel
			btm_brightness = (btm_r + btm_g + btm_b) // 3  # calculating the brightness of the pixel on the bottom
	    
			constrast = abs(top_brightness - btm_brightness) # finding the contrast between the two  pixels
	
		if constrast > threshold:
			set_color(new_image, x, y, black)
		else:
			set_color(new_image, x, y, white)
	
	
		if y == (btm_pixel - 1): # Must -1 because it counts 0 to btm_pixel
			set_color(new_image, x, y, white)
    
	return new_image
"""
image = load_image(choose_file())
edge_image = detect_edges(image, 5)
show(edge_image)

"""

# flip_vertical----------------------------------------------------------------------------------------------------------------------
def flip_vertical(image: Image) -> Image:
	"""Author: khalifeh basiri
	Return a vertically flipped copy of the image.
       
	>>> image = load_image(choose_file())
	>>> flipped_image = flip_vertical(image)
	>>> show(flipped_image)
	"""
	new_image = copy(image)
	val = get_height(image) - 1
	for x, y, (r, g, b) in image:
		v_flip = create_color(r,g,b)
		set_color(new_image, x, val-y, v_flip)
	return new_image

# flip_horizontal----------------------------------------------------------------------------------------------------------------------
def flip_horizontal(image: Image) -> Image:
	""" Author: Jason Perrins
	Returns a horizontal flipped copy of the image.
       
	image = load_image(choose_file())
	>>> new_image = flip_horizontal(image)
	>>> show(new_image)
	"""
	new_image = copy(image)  # Creates a copy of an image
	val = get_width(image) - 1 # x value of the last pixel    
	for x, y, (r, g, b) in image: # loops through every pixel in the given image
		flip_image = create_color(r,g,b) # Calls RGB values within a given pixel 
		set_color(new_image, val-x, y, flip_image) # sets the location of the pixel
							#in the x coordinate to the 
							# oposite side of the image
	return new_image # returns the new image with the change in x coordinate 
			 # applied

# draw_curve; _interpolation-----------------------------------------------------------------
def _interpolation(coordinates: list) -> list:
	""" Author: Arun Ichsanow
	Gets the polynomials coefficients from the points
	
	>>> _interpolation([[0,3],[2,2],[3,3])
	[0.5, -1.5, 3]
	"""
	xy_list = get_x_y_lists(coordinates) # splits the coordinates into 2 lists      
	x = xy_list[0] # xy_list[0] = all x values
	y = xy_list[1]# xy_list[1] = the corresponding y's
	pl = np.polyfit(x,y,len(x)-1).tolist() # finds coefficients and transforms
					       # them from an array [1 2 3] to a list [1,2,3]
	return pl

# draw_curve; _exhaustive_search-------------------------------------------------------------
def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> list:
	""" Author: Arun Ichsanow
	Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
	coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
	Returns None if there is no solution between the bounds.
       
	>>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
	253
	>>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
	590
	>>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
	None
	"""
	EPSILON = 1
	step = 1
	zeroes = []
    
	while abs(np.polyval(polycoeff, val)) >= EPSILON and val <= max_x: 
		val += step
	if val > max_x: 
		return None 
	else: return val

# draw_curve; _image_border_finding---------------------------------------------------------
def _image_border_finding(size: list, coefficients: list) -> list:
	""" Author: Arun Ichsanow
	Finds a point where the line crosses a border
	
	>>> _image_border_finding([5,5],[0.5, -1.5, 3])
	1
	"""
	
	point = _exhaustive_search(size[0]-1, coefficients, 0) # finds a point where
							       # the line crosses a
							       # border
	return point
   
# draw_curve-------------------------------------------------------------------------------
def draw_curve(image: Image, col: str, pointlist: list = None) ->  tuple:
	""" Author: Arun Ichsanow
	Allows the user to draw a curve on an image based on user input coordinates
	and a choosen colour.
	
	>>> draw_curve(image, cyan)
	The curve crosses a horizontal border at pixel 603.
	
	>>> draw_curve(image, black, test)
	The curve crosses a horizontal border at pixel 1.
	"""
	# creating the colours that were given in the manual------------------------
	black = create_color(0,0,0) 
	white = create_color(255,255,255)
	blood = create_color(255,0,0)
	green = create_color(0,255,0)
	blue = create_color(0,0,255)
	lemon = create_color(255,255,0)
	cyan = create_color(0,255,255)
	magenta = create_color(255,0,255)
	gray = create_color(128,128,128)
	
	# Create lists that are used to identify the user input colours and
	# determine their rgb values -----------------------------------------------    
	colours_possible_input = ["black", "white", "blood", "green", "blue", 
	                          "lemon", "cyan", "magenta", "gray"] # list of all 
								      # accepted
								      # inputs
	colours_rgb = [black, white, blood, green, blue, lemon, cyan, magenta, gray]
	# list of all possible inputs as Color types as per py
	
	for i in range(9): # runs the loop for each possible colour
		if col == colours_possible_input[i]: # compares the
						 # input colours to
						 # the list of
						 # possible colours
			colour = colours_rgb[i] # assigns the corresponding rgb value
					# to the current tone
					
	# Get image dimensions------------------------------------------------------
	width = get_width(image) # gets the width
	height = get_height(image) # gets teh height
	size = [width, height] # puts the width and height into a list
    
	if pointlist == None: #checks for 3rd parameter
		# notify user of size--------------------------------------------------- 
		print("Your image is", width, "pixels wide and", height, "pixels high.")
		
		# Ask the user how many points they want to provide-------------------------
		points = int(input("Please input the number of points you would like to\
provide.\nThe number should be at least 2.\n"))
        
		# Ask the user to provide the coordinates-----------------------------------
		coords = [] # list for all the coordinates
		for i in range(points): # lets them input the number of coordinates they
				    # chose previously
			single_coord = tuple(map(int,input("Enter the x and y value of your\
coordinate seperating them with a space: ").strip().split()))[:points] 
			coords.append(single_coord)
			# ^^ lets the user iput bot x and y coordinate on teh same line
	else: # if the 3rd parameter is present (for testing)
		coords = [[0,4],[2,0],[3,3]] # hardcoded test values
	
	# interpolation-------------------------------------------------------------
	sorted_coords = sort_points(coords) # sorts the coords by increasing x values
	coefficients = _interpolation(sorted_coords) # passes the sorted coords into
						     # auxilary function
	
	# _image_border_finding-----------------------------------------------------
	point_of_i = _image_border_finding(size, coefficients)
	# finds a point where the curve interstects the image border
    
	# drawing the curve---------------------------------------------------------
	edit_image = copy(image) # creates a copy of the input image
	if pointlist == None: # checks for 3rd parameter
		for x, y, (r, g, b) in edit_image: # runs loop for every pixel
			if int(np.polyval(coefficients, x)) == y: # checks if the pixel is
								  # on the curve
				for i in range(-2,3): # to make teh linewidth 5
					for j in range(-2,3): # to make teh linewidth 5
						if abs(i * j) != 4: # creates a circle with diameter 5
							if 0 <= x+i <= width-1 and 0 <= y+j <= height:
							# prevents Cimpl from trying to acces out-of-range
							# pixels
								set_color(edit_image, x+i, y+j, colour)
								# sets the colour of the pixels on the curve
	else: # for testing
		   # same as above but linewidth is 1 pixel for a smaller image 
		for x, y, (r, g, b) in edit_image: # runs loop for every pixel
			if int(np.polyval(coefficients, x)) == y: # checks if the pixel is
								  # on the curve
				set_color(edit_image, x, y, colour) # sets the colour of
								      # the pixel        
	result = (edit_image, point_of_i) # tuple containing the image and the 
					  # point of intersection (POI) w/ border
	return result