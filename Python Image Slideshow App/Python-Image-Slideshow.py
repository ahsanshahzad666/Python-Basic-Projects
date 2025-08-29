from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk


root = tk.Tk()
root.title("IMG SLIDESHOW VIWER")  

# list of images
images_path = [
   r"C:\Users\ahsan\Downloads\Blue-Hooide-TT010805-Models-online-129-2.webp",
   r"C:\Users\ahsan\Downloads\TT010805-Models-Print-84-scaled.webp",
   r"C:\Users\ahsan\Downloads\TT010805-Models-online-7.webp",
   r"C:\Users\ahsan\Downloads\linden-tee-shirt-1.webp"
]

# Resize and convert to Tkinter images
images_size = (1080,1080)
images = [Image.open(path). resize(images_size) for path in images_path]
photo_images = [ImageTk.PhotoImage(image) for image in images]




# Label to display images
label = tk.Label(root)
label.pack()


# Function to update images
def update_images():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)


slideshow = cycle(photo_images)



# Function to start slideshow 
def start_slideshow(): 
    for _ in range(len(images_path)): 
     update_images()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()



# Run Tkinter main loop
root.mainloop()