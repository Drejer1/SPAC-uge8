from Models.CerealProduct import CerealProduct
import mysql.connector # type: ignore

#This file is run on its own if the database needs the data from Cereal.csv again

connector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "250909"
)
connector.database = "cereal_database"
cursor = connector.cursor(dictionary=True)


with open("Data\\Cereal.csv", "r") as file:
    next(file)
    next(file)
    for line in file:
        splitLines = line.split(";") 
        print(splitLines[0])
        cursor.execute( f"SELECT * FROM cereal_database.cereal_product WHERE ProductName = '{splitLines[0].replace("'","''")}';")
        result = cursor.fetchall()
        if bool(result):
            continue
        cereal = CerealProduct(
            name=splitLines[0],
            mfr=splitLines[1],
            _type=splitLines[2],
            calories=int(splitLines[3]),
            protein=int(splitLines[4]),
            fat=int(splitLines[5]),
            sodium=int(splitLines[6]),
            fiber=float(splitLines[7]),
            carbo=float(splitLines[8]),
            sugars=int(splitLines[9]),
            potass=int(splitLines[10]),
            vitamins=int(splitLines[11]),
            shelf=int(splitLines[12]),
            weight=float(splitLines[13]),
            cups=float(splitLines[14]),
            rating=float((splitLines[15]).replace(".",""))
        )
        cursor.execute(cereal.to_insertion_query())
connector.commit()

cursor.close()