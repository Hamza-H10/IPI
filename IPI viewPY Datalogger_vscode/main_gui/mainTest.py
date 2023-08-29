import tkinter as tk
from tkinter import font, filedialog, messagebox
from db_connector import connect, execute_query

class MainForm:
    def __init__(self, root):
        self.root = root
        self.root.title("RS-485 Data Logger")
        self.root.geometry("700x600")

        self.init_ui()

        self.connection = connect()

    def init_ui(self):
        self.root.config(bg="#f0f0f0")

        segoe_font = font.Font(family="Segoe UI", size=12)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Import CSV", command=self.tb_import_click)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        button_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Buttons", menu=button_menu)
        button_menu.add_command(label="Back", command=self.tb_back_click)
        button_menu.add_command(label="Delete", command=self.tb_delete_click)
        button_menu.add_command(label="Graph", command=self.tb_view_graph_click)
        button_menu.add_command(label="Report", command=self.tb_report_click)
        button_menu.add_command(label="Base File", command=self.tb_base_file_click)
        
        self.root.bind("<Escape>", lambda event: self.root.quit())

        label = tk.Label(self.root, text="Welcome, user!", font=segoe_font, bg="#f0f0f0")
        label.pack(pady=(30, 10), fill="both", expand=True)
        
        # for back
        back_button = tk.Button(self.root, text="Back", command=self.tb_back_click)
        back_button.pack()
        
        # for delete
        delete_button = tk.Button(self.root, text="Delete", command=self.tb_delete_click)
        delete_button.pack()
        
        #for graph
        graph_button = tk.Button(self.root, text="Graph", command=self.tb_view_graph_click)
        graph_button.pack()
        
        #for report
        report_button = tk.Button(self.root, text="Report", command=self.tb_report_click)
        report_button.pack()

        #for Base file
        base_file_button = tk.Button(self.root, text="Base File", command=self.tb_base_file_click)
        base_file_button.pack()

    # def tb_import_click(self):
    #     file_path = filedialog.askopenfilename()
    #     if file_path and self.connection:
    #         query = f"LOAD DATA LOCAL INFILE '{file_path}' INTO TABLE csv_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES;"
    #         if execute_query(self.connection, query):
    #             messagebox.showinfo("Info", "CSV data imported successfully!")

    def tb_back_click(self):
        if self.connection:
            query = "UPDATE your_table_name SET your_column_name = your_new_value WHERE your_condition;"
            if execute_query(self.connection, query):
                messagebox.showinfo("Info", "Back button action executed successfully!")

    def tb_delete_click(self):
        if self.connection:
            # Customize the query according to your table structure and conditions
            query = "DELETE FROM your_table_name WHERE your_condition;"
            if execute_query(self.connection, query):
                messagebox.showinfo("Info", "Delete button action executed successfully!")

# -----------------------------------------------------------------------
    def tb_view_graph_click(self):
        if self.connection:
            # Customize the query according to your table structure and conditions
            query = "SELECT * FROM your_table_name WHERE your_condition;"
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()

                # Process the 'result' data and display the graph
                self.display_graph(result)
            except Error as e:
                messagebox.showerror("Error", f"Error: {e}")

    def display_graph(self, data):
        # Add code to display the graph using 'data'
        pass
# ---------------------------------------------------------------------------

    def tb_report_click(self):
        if self.connection:
            # Customize the query according to your table structure and conditions
            query = "SELECT * FROM your_table_name WHERE your_condition;"
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()

                # Generate and display the report
                self.generate_report(result)
            except Error as e:
                messagebox.showerror("Error", f"Error: {e}")

    def generate_report(self, data):
        # Add code to generate and display the report using 'data'
        pass
# ------------------------------------------------------------

    def tb_base_file_click(self):
        if self.connection:
            # Customize the query according to your table structure and conditions
            query = "SELECT * FROM your_table_name WHERE your_condition;"
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()

                # Process the 'result' data and perform the base file action
                self.perform_base_file_action(result)
            except Error as e:
                messagebox.showerror("Error", f"Error: {e}")

    def perform_base_file_action(self, data):
        # Add code to perform the base file action using 'data'
        pass

root = tk.Tk()
app = MainForm(root)
root.mainloop()
