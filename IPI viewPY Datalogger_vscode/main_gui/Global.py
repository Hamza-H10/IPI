# import mysql.connector

# class BoreHole:
#     def __init__(self):
#         self.Id = None
#         self.SiteName = None
#         self.Location = None
#         self.Depth = None
#         self.BaseFile = None

# def open_database():
#     db_config = {
#         'user': 'your_username',
#         'password': 'your_password',
#         'host': 'localhost',
#         'database': 'your_database_name',
#     }
    
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Boreholes (
#             Id INT PRIMARY KEY,
#             SITENAME VARCHAR(256),
#             LOCATION VARCHAR(256),
#             DEPTH DOUBLE NOT NULL,
#             BASEFILE VARCHAR(256)
#         )
#     """)
#     connection.commit()

#     return connection, cursor

# def close_database(connection):
#     connection.close()

# def add_borehole(connection, cursor, bh):
#     try:
#         cursor.execute("""
#             INSERT INTO Boreholes (Id, SITENAME, LOCATION, DEPTH, BASEFILE)
#             VALUES (%s, %s, %s, %s, %s)
#         """, (bh.Id, bh.SiteName, bh.Location, bh.Depth, ''))
#         connection.commit()
#         return True
#     except:
#         return False

# def update_borehole(connection, cursor, bh):
#     bn_add_base_file = len(bh.BaseFile) >= 2
#     if bn_add_base_file:
#         cursor.execute("""
#             UPDATE Boreholes
#             SET SITENAME = %s, LOCATION = %s, DEPTH = %s, BASEFILE = %s
#             WHERE Id = %s
#         """, (bh.SiteName, bh.Location, bh.Depth, bh.BaseFile, bh.Id))
#     else:
#         cursor.execute("""
#             UPDATE Boreholes
#             SET SITENAME = %s, LOCATION = %s, DEPTH = %s
#             WHERE Id = %s
#         """, (bh.SiteName, bh.Location, bh.Depth, bh.Id))
#     connection.commit()
#     return True

# def delete_borehole(connection, cursor, id):
#     cursor.execute("DELETE FROM Boreholes WHERE Id = %s", (id,))
#     connection.commit()

# def get_boreholes(cursor):
#     cursor.execute("SELECT Id, SITENAME, LOCATION, DEPTH, BASEFILE FROM Boreholes ORDER BY Id")
#     rows = cursor.fetchall()
#     boreholes = []
#     for row in rows:
#         bh = BoreHole()
#         bh.Id, bh.SiteName, bh.Location, bh.Depth, basefile = row
#         bh.BaseFile = "" + basefile
#         boreholes.append(bh)
#     return boreholes

# def read_csv_file(file_name):
#     data = []
#     try:
#         with open(file_name, 'r') as file:
#             for line in file:
#                 split = line.strip().split(',')
#                 data.append(split)
#         return data
#     except Exception as ex:
#         print(str(ex))
#         return None

# def get_borehole_directory(bh_num):
#     return f"{bh_num:02}"

# if __name__ == "__main__":
#     connection, cursor = open_database()

#     # # Create and populate a sample BoreHole object
#     # bh = BoreHole()
#     # bh.Id = 1
#     # bh.SiteName = "Sample Site"
#     # bh.Location = "Sample Location"
#     # bh.Depth = 100.0
#     # bh.BaseFile = "sample_file.txt"

#     # # Add the sample BoreHole object to the database
#     # add_borehole(connection, cursor, bh)

#     # # Update the sample BoreHole object in the database
#     # bh.SiteName = "Updated Site"
#     # update_borehole(connection, cursor, bh)

#     # # Retrieve all boreholes from the database
#     # boreholes = get_boreholes(cursor)
#     # for bh in boreholes:
#     #     print(f"Id: {bh.Id}, SiteName: {bh.SiteName}, Location: {bh.Location}, Depth: {bh.Depth}, BaseFile: {bh.BaseFile}")

#     # # Delete the sample BoreHole object from the database
#     # delete_borehole(connection, cursor, bh.Id)


#     close_database(connection)
