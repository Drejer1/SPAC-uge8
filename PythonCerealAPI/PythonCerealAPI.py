from re import I
from ServerConnection import DBmanager
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
dbm = DBmanager()

@app.route('/', methods =['GET'])
def get_test():
    return jsonify("TEST TEST")

@app.route('/products', methods=['GET'])
def get_product():

    filt = request.args.to_dict()
    return jsonify(dbm.get_product(filt))

@app.route('/products', methods =['DELETE'])
def delete_product():
    ID = request.args.get('ID',type=int)
    if ID:
        dbm.deleteProductByID(ID)
        return "Entry deleted", 200
    return "ID not provided", 400

@app.route('/products', methods =['POST'])
def update_product():
    product_data = request.get_json()
    if "ID" in product_data: 
        if dbm.get_check_exists(int(product_data["ID"])):
            dbm.updateProduct(product_data)
            return "Entry updated",200
        else:
            return "Cant specifically define the ID on non-existant entry", 400

    if dbm.check_name_available(product_data["ProductName"]):
        dbm.createNewProduct(product_data)
        return "New entry in DB created",200
    else: return "Name already in DB" ,400

@app.route('/productPicture/<int:ID>',methods =['GET'])
def get_picture_of_product(ID):
    
    if ID: 
        if dbm.get_check_exists(ID):
            path = dbm.get_path(ID)
            return send_file(path) 

        else: return "Entry does not exist",400

    else:
        return "ID not provided", 400
    

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port="8000")

update_product("")
