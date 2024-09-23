import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import qrcode
import os

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x700")

# Variables to store the link and image path
link_var = tk.StringVar()
image_path_var = tk.StringVar()
use_image_var = tk.IntVar(value=0)  # 0 means image is required

# Label and Entry widget for the link input with padding
link_label = tk.Label(root, text="Enter the link:")
link_label.pack(pady=10, padx=20, anchor='w')  # Added padx and anchor

link_entry = tk.Entry(root, textvariable=link_var, width=50)
link_entry.pack(pady=5, padx=20)  # Added padx

# Function to browse and select an image
def browse_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if file_path:
        image_path_var.set(file_path)
        # Display the selected image
        img = Image.open(file_path)
        img.thumbnail((100, 100))
        img_display = ImageTk.PhotoImage(img)
        image_label.configure(image=img_display)
        image_label.image = img_display  # Keep a reference

# Label and Button to select the image
image_label_text = tk.Label(root, text="Select an image for the center of the QR code:")
image_label_text.pack(pady=10, padx=20, anchor='w')  # Added padx and anchor

image_button = tk.Button(root, text="Browse Image", command=browse_image)
image_button.pack(pady=5)

# Display selected image
image_label = tk.Label(root)
image_label.pack(pady=5)

# Checkbox to deactivate image requirement
def toggle_image_requirement():
    if use_image_var.get() == 1:
        image_button.config(state=tk.DISABLED)
        image_label.config(image='')
        image_label.image = None
        image_path_var.set('')
    else:
        image_button.config(state=tk.NORMAL)

checkbox = tk.Checkbutton(
    root,
    text="Do not use an image in the QR code",
    variable=use_image_var,
    command=toggle_image_requirement,
    onvalue=1,
    offvalue=0
)
checkbox.pack(pady=10, padx=20, anchor='w')  # Added padx and anchor

# Function to generate the QR code
def generate_qr():
    global qr_img
    link = link_var.get()
    image_path = image_path_var.get()
    if link == '':
        messagebox.showerror("Error", "Please enter a link.")
    elif use_image_var.get() == 0 and image_path == '':
        messagebox.showerror("Error", "Please select an image or check the option to not use one.")
    else:
        # Generate QR code
        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        if use_image_var.get() == 0 and image_path != '':
            # Open the logo image
            logo = Image.open(image_path)

            # Calculate the size of the logo
            qr_width, qr_height = img_qr.size
            logo_size = int(qr_width / 3)
            logo.thumbnail((logo_size, logo_size))

            # Calculate coordinates to center the logo
            logo_pos = (
                (qr_width - logo.size[0]) // 2,
                (qr_height - logo.size[1]) // 2
            )

            # Paste the logo onto the QR code
            img_qr.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)

        # Save the image to a temporary file
        img_qr.save("qr_code_temp.png")

        # Display the QR code in the GUI
        img_display = ImageTk.PhotoImage(img_qr.resize((200, 200)))
        img_label.configure(image=img_display)
        img_label.image = img_display  # Keep a reference

        # Enable the Save button
        save_button.config(state=tk.NORMAL)
        qr_img = img_qr  # Store the image for saving

# Function to save the QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
    )
    if file_path:
        # Ensure the file has a .png extension
        if not file_path.lower().endswith('.png'):
            file_path += '.png'
        qr_img.save(file_path)
        messagebox.showinfo("Saved", "QR Code saved successfully!")

# Button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Label to display the QR code image
img_label = tk.Label(root)
img_label.pack(pady=10)

# Button to save the QR code
save_button = tk.Button(root, text="Save QR Code", command=save_qr, state=tk.DISABLED)
save_button.pack(pady=5)

# Run the application
root.mainloop() # Run the main loop of the application