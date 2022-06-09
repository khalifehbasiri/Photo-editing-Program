from filter_program import *
from Cimpl import *


def check(inputs: str):
  options = ["L", "l", "S", "s", "3", "X", "x", "T", "t", "P", "p", "E", "e", "D",\
          "d", "V", "v", "H", "h", "Q", "q"]  
  check = False
  for i in range(21):
    if choice == options[i]:
      check = True
      return True
            
  if check == False:
    print("No such command")
    return False

def _load() -> Image:
  """
  loads the user input image.
     
  >>> load()
  """
  image_orig = load_image(choose_file())  # loads the image
  image_new = copy(image_orig)
  return image_new # returns original image. It is unessecary to copy the
                    # image since it is saved as a new file.
                    
def save(image_new: Image):
  """
  saves the image under a user input name
  
  >>> save(image, test1.jpg)
  """
  save_as(image_new)  # saves image under its new name

                   
def apply_filter(string:str, image: Image = None) -> int:
  all_filters = [extreme_contrast, sepia, posterize, flip_vertical, flip_horizontal] # all filters within the batch file except for 
                                  # 3-tone and edge detection
  options = ["X", "x", "T", "t", "P", "p", "V", "v", "H", "h"] # all filter inputs
                                                               # within the batch
                                                               # file except for 
                                                               # 3-tone and edge
                                                               # detection
  if choice == "L" or choice == "l":
    image = _load()
    
  elif string == '3': # if 3-tone filter is called (since it requires hard-
                       # coded "user input")
    if image == None:
        print("No image loaded")
        return None
    image = three_tone(image, "gray", "lemon", "blood") #3-tone filter
    show(image)
    
  elif string == "E" or string == "e": # if edge detection filter is 
                                              # called (since it requires hard-
                                              # coded "user input")
    if image == None:
        print("No image loaded")
        return None
    threshold = int(input("\nPlease input the threshold value you would like to use: "))
    image = detect_edges(image, threshold)
    show(image)
    
  elif string == "D" or string == "d":
    if image == None:
        print("No image loaded")
        return None
    new_tuple = draw_curve(image, "cyan")
    image = new_tuple[0]
    print(new_tuple[1])
    show(image)
    
  else: # every other filter
    if image == None:
        print("No image loaded")
        return None
    for j in range(len(options)): # converts the filter input letter into the
                                # corresponding filter
      if string == options[j]:
        image = all_filters[int(j / 2)](image) # (j/2) because each filter has 2 
                                           # possible inputs, upper- and lower-
                                           # case
    show(image)
  return image    




command = True
image = None
while command == True: # loops through these steps until the user prompts to quit
    choice = str(input("\n\nL)oad\tS)ave\n3)-tone\tX)treme contrast\tT)int sepia\tP)osterize\
\nE)dge detection\tD)raw curve\tV)ertical flip\tH)orizontal flip\nQ)uit\n\n:< > "))
    if check(choice) == True:
      if choice == "Q" or choice == "q":
        print("Quit")
        command = False
      elif choice == "S" or choice == "s":
        save(image)
      else:
        image = apply_filter(choice, image)