import tkinter as tk
from tkinter import font
from window_code import create_menu_bar


# Create the main application window
root = tk.Tk()
root.title("𝐑𝐒-𝟒𝟖𝟓 Data Logger")
root.geometry("700x600")

# Load the Segoe UI font
segoe_font = font.Font(family="Segoe UI", size=12)

# Set the window background color
root.config(bg="#f0f0f0")

# Create a label widget with centered text and Segoe UI font
label = tk.Label(root, text="welcome, user!", font=segoe_font, bg="#f0f0f0")
label.pack(pady=20, fill="both", expand=True)

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="Button clicked!")
    
# Set the window icon using a .ico file
icon_path = "icon.ico"  # Replace with the path to your .ico file
root.iconbitmap("D:\IPI viewPY Datalogger_vscode\main_gui\icon.ico")

# Create a button widget with Windows 11-style appearance
button = tk.Button(
    root,
    text="Login!",
    command=button_click,
    font=segoe_font,
    bg="#0078D4",
    fg="white",
    activebackground="#005A9E",
    activeforeground="white",
)
button.pack(fill="both", padx=20, pady=(0, 20))

# Apply rounded corners to the button
button["borderwidth"] = 0
button["highlightthickness"] = 0
button["relief"] = "flat"
button["highlightbackground"] = "#f0f0f0"

# Call the function to create the GUI window
create_menu_bar(root)

# Start the main event loop
root.mainloop()


# font that can be used: Helvetica / Arial   Roboto  Open Sans   Lato    Montserrat  Source Sans Pro Nunito  Poppins Avenir