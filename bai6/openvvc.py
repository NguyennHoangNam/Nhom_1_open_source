import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog

# Function to rotate the image
def rotate_image():
    global rotated_image_label
    global input_angle_entry

    angle = int(input_angle_entry.get())

    # Rotate the image
    rotated = cv2.rotate(cv2_image, cv2.ROTATE_90_CLOCKWISE)

    # Convert the rotated image to PIL format
    pil_image = Image.fromarray(rotated)

    # Create a Tkinter-compatible image to display inside the rotated image label
    rotated_image = ImageTk.PhotoImage(pil_image)

    # Update the rotated image label
    rotated_image_label.configure(image=rotated_image)
    rotated_image_label.image = rotated_image

# Function to open the file dialog for image selection
def open_image():
    global cv2_image
    global original_image_label
    global rotated_image_label

    # Open the file dialog to select an image file
    file_path = filedialog.askopenfilename()

    if file_path:
        # Read the image using OpenCV
        cv2_image = cv2.imread(file_path)

        # Convert the OpenCV image to PIL format
        pil_image = Image.fromarray(cv2_image)

        # Create a Tkinter-compatible image to display inside the original image label
        original_image = ImageTk.PhotoImage(pil_image)

        # Update the original image label
        original_image_label.configure(image=original_image)
        original_image_label.image = original_image

        # Clear the rotated image label
        rotated_image_label.configure(image=None)
        rotated_image_label.image = None

# Create the main application window
window = tk.Tk()
window.title("Image Rotator")

# Create an image label to display the original image
original_image_label = tk.Label(window)
original_image_label.pack()

# Create an image label to display the rotated image
rotated_image_label = tk.Label(window)
rotated_image_label.pack()

# Create a button to open the file dialog for image selection
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

# Create a label and entry for inputting the rotation angle
input_angle_label = tk.Label(window, text="Rotation Angle:")
input_angle_label.pack()

input_angle_entry = tk.Entry(window)
input_angle_entry.pack()

# Create a button to rotate the image
rotate_button = tk.Button(window, text="Rotate", command=rotate_image)
rotate_button.pack()

# Start the Tkinter event loop
window.mainloop()