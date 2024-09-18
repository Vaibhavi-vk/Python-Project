from tkinter import *
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd 
import cv2
root = tk.Tk()
root.geometry('400x500')
root.configure(background='deep pink')
#Remove maximize option
root.resizable(0,0)
#Create class
class imageEditor:
#Create Functions
  def callback():
    global img, name, filesave
    name = fd.askopenfilename() 
    img = cv2.imread(name)
    cv2.imshow('Image', img)
   # cv2.waitkey(0)
  errmsg = 'Error!'
  label = tk.Label(root, text = "Image Editor", bg="yellow", fg="red",relief = RAISED, font=("Bodoni MT Black", 18), height=2, width=13).pack(side='top', expand="YES")  
  btn1=tk.Button(root, text='Click to Open File', command=callback, bg="blue", fg="white", font=("Bahnschrift Semibold",13)).pack(side='top')
  def resizeImage():
      img = Image.open(name)
      w = sd.askinteger("Input values", "Please enter width")
      h = sd.askinteger("Input values", "Please enter height")
      resized_img = img.resize((round(img.size[0]-w), round(img.size[1]-h)))
      resized_img.save('Resized.jpg')
      resized_img.show()
  btn2=tk.Button(root, text='Resize image', command=resizeImage, bg="blue", fg="white", font=("Bahnschrift Semibold",13)).pack(side='left', expand=("YES"))
  def rotateImage():
      img = Image.open(name)
      angle = sd.askinteger("Input value", "Please enter angle value to rotate")
      rotate_img = img.rotate(angle)
      rotate_img.save('Rotateimg.jpg')
      rotate_img.show()
  btn3=tk.Button(root, text='Rotate image', command=rotateImage, bg="blue", fg="white", font=("Bahnschrift Semibold",13)).pack(side='right', expand=("YES"))
  def cropImage():
      img = Image.open(name)
      l = sd.askinteger("Input values", "Please enter value for left")
      t = sd.askinteger("Input values", "Please enter value for top")
      r = sd.askinteger("Input values", "Please enter right")
      b = sd.askinteger("Input values", "Please enter bottom")
      area = (l,t,r,b)
      crop_img = img.crop((area))
      crop_img.save('Cropimg.jpg')
      crop_img.show()
  btn4=tk.Button(root, text='Crop image', command=cropImage, bg="blue", fg="white", font=("Bahnschrift Semibold",13)).pack(side='bottom', expand=("YES"))
  def blur():
      #Create image object
      img = Image.open(name)
      #Applying the blur filter
      blur_img = img.filter(BLUR)
      blur_img.save('blurimg.jpg')
      blur_img.show()
  def sketch():
      #Create image object
      img = Image.open(name)
      #Applying the sketch filter
      sketch_img = img.filter(CONTOUR)
      sketch_img.save('sketchimg.jpg')
      sketch_img.show()
  def detail():
      img = Image.open(name) 
      detail_img = img.filter(DETAIL)
      detail_img.save('Detailimg.jpg')
      detail_img.show()
  def enhance_edge():
      img = Image.open(name)
      enhance_edge = img.filter(EDGE_ENHANCE)
      enhance_edge.save('enhance_edgeimg.jpg')
      enhance_edge.show()
  def enhance_edgemore():
      img = Image.open(name)
      enhance_edgemore = img.filter(EDGE_ENHANCE_MORE)
      enhance_edgemore.save('EDGE_ENHANCE_MORE.jpg')
      enhance_edgemore.show()
  def emboss():
      img = Image.open(name)
      emboss = img.filter(EMBOSS)
      emboss.save('EMBOSS.jpg')
      emboss.show()
  def find_edges():
      img = Image.open(name)
      find_edges = img.filter(FIND_EDGES)
      find_edges.save('FIND_EDGES.jpg')
      find_edges.show()
  def sharpen():
      img = Image.open(name)
      sharpen = img.filter(SHARPEN)
      sharpen.save('SHARPEN.jpg')
      sharpen.show()
  def smooth():
      img = Image.open(name)
      smooth = img.filter(SMOOTH)
      smooth.save('SMOOTH.jpg')
      smooth.show()
  def smoothmore():
      img = Image.open(name)
      smoothmore = img.filter(SMOOTH_MORE)
      smoothmore.save('SMOOTH_MORE.jpg')
      smoothmore.show()
  menubutton =tk.Menubutton(root, text = "Filters->", bg="blue", fg="white", font=("Bahnschrift Semibold",13), relief = RAISED)    
  menubutton.menu = Menu(menubutton)  
  menubutton["menu"]=menubutton.menu  
  menubutton.menu.add_checkbutton(label = "blur", variable = IntVar(), command=blur)  
  menubutton.menu.add_checkbutton(label = "Sketch", variable=IntVar(), command=sketch)
  menubutton.menu.add_checkbutton(label = "Detail", variable=IntVar(), command=detail)
  menubutton.menu.add_checkbutton(label = "Enhance_Edge", variable=IntVar(), command=enhance_edge)  
  menubutton.menu.add_checkbutton(label = "Enhance_EdgeMore", variable=IntVar(), command=enhance_edgemore)
  menubutton.menu.add_checkbutton(label = "Emboss", variable=IntVar(), command=emboss)
  menubutton.menu.add_checkbutton(label = "FindEdeges", variable=IntVar(), command=find_edges)
  menubutton.menu.add_checkbutton(label = "Sharpen", variable=IntVar(), command=sharpen)
  menubutton.menu.add_checkbutton(label = "Smooth", variable=IntVar(), command=smooth)
  menubutton.menu.add_checkbutton(label = "Smoothmore", variable=IntVar(), command=smoothmore)
  menubutton.pack(side='top', expand=("YES")) 
root.mainloop()



  





