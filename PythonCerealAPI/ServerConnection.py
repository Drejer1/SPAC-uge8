import mysql.connector

class DBmanager():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBmanager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.connection = self._create_connection()
        self._initialized = True
        

    def _create_connection(self):
        return mysql.connector.connect(
            host = "192.168.87.103",
            user = "root",
            password = "250909"
        )

    def _get_cursor(self):
        return self.connection.cursor(dictionary=True)

    def get_check_exists(self,ID:int):
        cursor = self._get_cursor()
        cursor.execute(f'SELECT * FROM cereal_database.cereal_product WHERE ID ={ID};')
        result = cursor.fetchall()
        return bool(result)

    def get_product(self,filt:dict):
        cursor = self._get_cursor()
        if  not bool(filt):
            cursor.execute('SELECT * FROM cereal_database.cereal_product;')
            result = cursor.fetchall()
            cursor.close()
            return result
        query = "SELECT * FROM cereal_database.cereal_product WHERE "
        conditions = []
        for key, value in filt.items():
            if key.startswith('gt_'):
                column = key[3:]
                conditions.append(f"{column} > {value}")
            elif key.startswith('lt_'):
                column = key[3:]
                conditions.append(f"{column} < {value}")
            else:
                conditions.append(f"{key} = {value}")
        query += " AND ".join(conditions)
        query +=";"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def deleteProductByID(self, ID):
        cursor = self._get_cursor()
        query = f"DELETE FROM cereal_database.cereal_product WHERE ID = {ID}"
        cursor.execute(query)
        self.connection.commit()

    def createNewProduct(self, product_data: dict):
        cursor = self._get_cursor()
        query = f"""
        INSERT INTO cereal_database.cereal_product 
        (ProductName, Mfr, TypeVarmOrCold, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating)
        VALUES ('{product_data["ProductName"]}', '{product_data["Mfr"]}', '{product_data["TypeVarmOrCold"]}', {product_data["calories"]}, {product_data["protein"]}, {product_data["fat"]}, {product_data["sodium"]}, {product_data["fiber"]}, {product_data["carbo"]}, {product_data["sugars"]}, {product_data["potass"]}, {product_data["vitamins"]}, {product_data["shelf"]}, {product_data["weight"]}, {product_data["cups"]}, {product_data["rating"]})
        """
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def updateProduct(self,product_data):
        cursor = self._get_cursor()
        query = "UPDATE cereal_database.cereal_product SET "
        for key, value in product_data.items():
            if key == "ID":
                continue
            query+= f" {key} = '{value}',"
        query = query.rstrip(query[-1])
        query+= f" WHERE ID = {product_data["ID"]};"

        cursor.execute(query)
        self.connection.commit()
        cursor.close()
        
    def check_name_available(self,name:str):
        cursor = self._get_cursor()
        cursor.execute( f"SELECT * FROM cereal_database.cereal_product WHERE ProductName = '{name.replace("'","''")}';")
        result = cursor.fetchall()
        cursor.close()
        return not bool(result)

    def get_path(self,ID):
        cursor = self._get_cursor()
        cursor.execute(f"SELECT pathToPicture FROM cereal_database.cereal_product WHERE ID = {ID}")
        result = cursor.fetchone()
        return result["pathToPicture"]
        
    