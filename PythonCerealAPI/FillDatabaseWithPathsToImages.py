import mysql.connector # type: ignore
import os

#This file is run strictly to assoicate the pictures to the corresponding cereal product in Cereal.csv
connector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "250909"
)
connector.database = "cereal_database"
cursor = connector.cursor(dictionary=True)
pathToPictures = os.path.join("Data", "Cereal Pictures\\")


def findAssociatedPath(name: str):
    extensions = [".jpg", ".png"]
    possible_names = [name, name.replace(" ", "")]
        
    for ext in extensions:
        for pname in possible_names:
            full_path = os.path.join(pathToPictures, pname + ext)
            if os.path.exists(full_path):
                return full_path.replace("\\","\\\\")
    return None
 
query="SELECT ID, ProductName FROM cereal_database.cereal_product"
cursor.execute(query)

result = cursor.fetchall()
for entry in result: 
    path = findAssociatedPath(entry["ProductName"])
    print(path)
    if not path == None:
        querySetPath = f"UPDATE cereal_database.cereal_product SET pathToPicture = '{path.replace("'","''")}' WHERE ID = {int(entry["ID"])}"
        cursor.execute(querySetPath)
        connector.commit()
cursor.close()

