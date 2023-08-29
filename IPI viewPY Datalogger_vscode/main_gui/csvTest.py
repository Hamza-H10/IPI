import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class Measurement:
    def __init__(self, timestamp, machine_id, sensor_number, sensor_value1, sensor_value2):
        self.timestamp = timestamp
        self.machine_id = machine_id
        self.sensor_number = sensor_number
        self.sensor_value1 = sensor_value1
        self.sensor_value2 = sensor_value2

def import_data():
    cnt = 0
    cnt_error = 0
    cnt_repeat = 0
    msg_string = "Import Summary:\n"

    file_names = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")])
    measurements = []
    
    for file_name in file_names:
        if file_name.lower().endswith(".csv"):
            with open(file_name, "r") as file:
                lines = file.readlines()
            if len(lines) < 1:
                cnt_error += 1
            else:
                machine_id = int(lines[0][len("MachineID: "):])

                for line in lines[1:]:
                    parts = line.split(",")
                    if len(parts) == 3:
                        try:
                            timestamp = parts[0].strip()
                            sensor_values = parts[1].strip().split(":")
                            sensor_value1 = float(sensor_values[1].strip())
                            sensor_value2 = float(sensor_values[2].strip())
                            sensor_number = int(parts[2].strip()[len(" Sensor: "):])
                            measurements.append(
                                Measurement(
                                    timestamp,
                                    machine_id,
                                    sensor_number,
                                    sensor_value1,
                                    sensor_value2,
                                )
                            )
                        except ValueError:
                            cnt_error += 1
                    else:
                        cnt_error += 1

                cnt += 1

    if cnt > 0:
        msg_string += f"You have added {cnt} CSV file(s) to the InclinoView successfully.\n"
    if cnt_error > 0:
        msg_string += f"{cnt_error} line(s) were found to be incorrect format.\n"
    if cnt_repeat > 0:
        msg_string += f"{cnt_repeat} file(s) were already imported into the application, hence ignored.\n"

    messagebox.showinfo("Import", msg_string)

    # Create a new window to display the data in a table
    data_window = tk.Toplevel(root)
    data_window.title("Imported Data Table")

    # Create a Treeview widget for displaying the data
    tree = ttk.Treeview(data_window, columns=("Timestamp", "Machine ID", "Sensor Number", "Sensor Value 1", "Sensor Value 2"))
    tree.heading("#1", text="Timestamp")
    tree.heading("#2", text="Machine ID")
    tree.heading("#3", text="Sensor Number")
    tree.heading("#4", text="Sensor Value 1")
    tree.heading("#5", text="Sensor Value 2")

    # Insert the data into the Treeview
    for measurement in measurements:
        tree.insert("", "end", values=(measurement.timestamp, measurement.machine_id, measurement.sensor_number, measurement.sensor_value1, measurement.sensor_value2))

    tree.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    import_data()
    root.mainloop()
