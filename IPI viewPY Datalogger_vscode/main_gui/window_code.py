import tkinter as tk

def create_menu_bar(root):
        # Create a menu bar with 3D effect
    menu_bar = tk.Menu(root, relief="flat", bg="#f0f0f0", activeborderwidth=0)
    root.config(menu=menu_bar)

    # Create File menu
    
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Create Data Logger menu with options
    data_logger_menu = tk.Menu(menu_bar, tearoff=0)
    data_logger_menu.add_command(label="Start Data Logger")
    data_logger_menu.add_command(label="Stop Data Logger")
    menu_bar.add_cascade(
        label="Data Logger", menu=data_logger_menu, background="#0078D4", foreground="white"
    )

    # Create Config Sensors menu with options
    config_sensors_menu = tk.Menu(menu_bar, tearoff=0)
    config_sensors_menu.add_command(label="Calibrate Sensors")
    config_sensors_menu.add_command(label="Set Thresholds")
    menu_bar.add_cascade(
        label="Config Sensors", menu=config_sensors_menu, background="#0078D4", foreground="white"
    )

    # Create Diagnostic menu with options
    diagnostic_menu = tk.Menu(menu_bar, tearoff=0)
    diagnostic_menu.add_command(label="Run Diagnostic Tests")
    menu_bar.add_cascade(
        label="Diagnostic", menu=diagnostic_menu, background="#0078D4", foreground="white"
    )

    # Create Settings menu with options
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(label="General Settings")
    settings_menu.add_command(label="Advanced Settings")
    menu_bar.add_cascade(
        label="Settings", menu=settings_menu, background="#0078D4", foreground="white"
    )

    # Create Help menu with options
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="User Manual")
    help_menu.add_command(label="About")
    menu_bar.add_cascade(
        label="Help", menu=help_menu, background="#0078D4", foreground="white"
    )

def button_click(menu_item):
    label.config(text=f"{menu_item} clicked!")


