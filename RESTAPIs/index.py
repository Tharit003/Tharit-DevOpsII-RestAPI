from flask import Flask, request, jsonify

app = Flask(__name__)

Items = [{"id":"1","name": "product name","category": "1","price": "20.5","instock":"200"}]

def _find_next_id(id: int):
    data = [x for x in Items if x['id'] == id]
    return data


#REST API
@app.route('/product', methods=["GET"])
def get_product():
    return jsonify(Items)

# GET -by ID
@app.route('/product/<id>', methods=["GET"])
def get_product_id(id):
    data = _find_next_id(id)
    return jsonify(data)


@app.route('/product/<id>', methods=["DELETE"])
def delete_product(id):

    data = _find_next_id(id)
    if not data:
        return {"error": "Product not found"}, 404
    else:
        Items.remove(data[0])
        return "Product deleted successfully", 200


@app.route('/product', methods=["POST"])
def post_product():
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "instock": instock    
    }

    if (_find_next_id(id)):
        return {"error": "Bad Request"}, id
    else:
        Items.append(new_data)
        return jsonify(Items)
    

@app.route('/product/<int:id>', methods=["PUT"])
def update_product(id: int):
    global Items
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
     
    update_data = {
        "id" : id,
        "name" : name,
        "category": category,
        "price": price,
        "instock": instock
    }

    for product in Items:
        if  id == product.get("id"):
            product["name"] = str(name)
            product["category"] = str(category)
            product["price"] = str(price)
            product["instock"] = str(instock)
            return jsonify(Items)
        else:
            return "Error", 404
        
@app.route('/patch_product/<id>', methods=["PATCH"])
def patch_product(id):
    id = request.form.get('id')
    global Items
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    data = _find_next_id(id)
    if not data:
        return {"error": "Product not found"}, 404

    name.form.get('name')
    category.form.get('category')
    price.form.get('category')
    instock.form.get('instock')

    if name:
        data['name'] = name
    if category:
        data['category'] = category
    if price:
        data['price'] = price
    if instock:
        data['instock'] = instock
    return {"message": "Product updated successfully"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

