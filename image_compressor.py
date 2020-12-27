import PIL
from PIL  import Image
from tkinter.filedialog import *

file_path=askopenfilename()
img = PIL.Image.open(file_path)
h,w=img.size

img = img.resize((h,w), PIL.Image.ANTIALIAS)

save_path = asksaveasfilename()

img.save(save_path+"__compressed__.JPG")
