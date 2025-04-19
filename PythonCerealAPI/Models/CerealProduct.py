
#Class for the cereal product was created incase it was ever to be used
#However it is only used in ParseAndInsert.py currently
class CerealProduct:
    def __init__(self, name:str, mfr:str, _type:str, calories:int, protein:int, fat:int, sodium:int, fiber:float, carbo:float, sugars:int, potass:int, vitamins:int, shelf:int, weight:float, cups:float, rating:float):
        self.name = name
        self.mfr = mfr
        self.type = _type
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.sodium = sodium
        self.fiber = fiber
        self.carbo = carbo
        self.sugars = sugars
        self.potass = potass
        self.vitamins = vitamins
        self.shelf = shelf
        self.weight = weight
        self.cups = cups
        self.rating = rating
    def to_insertion_query(self):
        query = ("INSERT INTO cereal_product (ProductName,Mfr,TypeVarmOrCold,calories,"
            "protein,fat,sodium,fiber,carbo,sugars,potass,vitamins,shelf,weight,cups,rating)" 
            f"VALUES('{self.name.replace("'","''")}','{self.mfr}','{self.type}','{self.calories}','{self.protein}','{self.fat}','{self.sodium}','{self.fiber}','{self.carbo}'"
            f",'{self.sugars}','{self.potass}','{self.vitamins}','{self.shelf}','{self.weight}','{self.cups}','{self.rating}');")
        return query
