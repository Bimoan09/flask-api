from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/penjualan'
mongo = PyMongo(app)

# Define collections
customers = mongo.db.customers
products = mongo.db.products
sales = mongo.db.sales

# Route to create a new customer
@app.route('/customer', methods=['POST'])
def add_customer():
    name = request.json['name']
    handphone = request.json['handphone']
    new_customer = {'name': name, 'handphone': handphone}
    customer_id = customers.insert_one(new_customer)
    response = {
        "message": "Customer successfully created",
        "customer_id": str(customer_id.inserted_id)
    }
    return jsonify(response), 201

# Route to retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    all_customers = customers.find()
    output = []
    for customer in all_customers:
        output.append({'_id' : str(customer['_id']), 'name': customer['name'], 'handphone': customer['handphone']})
    return jsonify({'customers': output}), 200

# Route to update customers
@app.route('/customer/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    request_data = request.get_json()
    updated_customer = {}
    for field in ['name', 'handphone']:
        if field in request_data:
            updated_customer[field] = request_data[field]
    # Convert customer_id to ObjectId
    customer_oid = ObjectId(customer_id)
    # Check if customer exists
    customer = mongo.db.customers.find_one({'_id': customer_oid})
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    # Update the customer with the new data
    mongo.db.customers.update_one({'_id': customer_oid}, {'$set': updated_customer})
    return jsonify({'message': 'Customer data updated'}), 200


# Route detail customer with ID
@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer_details(customer_id):
    # Convert customer_id to ObjectId
    customer_oid = ObjectId(customer_id)
    # Find the customer by ID
    customer = mongo.db.customers.find_one({'_id': customer_oid})
    if customer:
        # Return customer details
        return jsonify({
            '_id': str(customer['_id']),
            'name': customer['name'],
            'handphone': customer['handphone']
        }), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404

# Route delete customer
@app.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    # Convert customer_id to ObjectId
    customer_oid = ObjectId(customer_id)
    # Find the customer by ID
    customer = mongo.db.customers.find_one({'_id': customer_oid})
    if customer:
        # Delete the customer
        mongo.db.customers.delete_one({'_id': customer_oid})
        return jsonify({'message': 'Customer deleted successfully'}), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404
# End customer API



# Start Products API
# Route to create a new product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    unit_price = request.json['unit_price']
    stock = request.json['stock']
    new_product = {'name': name, 'unit_price': unit_price, 'stock': stock}
    product_id = products.insert_one(new_product)
    response = {
        "message": "Product successfully created",
        "product_id": str(product_id.inserted_id)
    }
    return jsonify(response), 201

# Route to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    all_products = products.find()
    output = []
    for product in all_products:
        output.append({'_id' : str(product['_id']),'name': product['name'], 'unit_price': product['unit_price'], 'stock': product['stock']})
    return jsonify({'products': output}), 200

# Route to Update products
@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    request_data = request.get_json()
    updated_product = {}
    for field in ['name', 'unit_price', 'stock']:
        if field in request_data:
            updated_product[field] = request_data[field]
    product_oid = ObjectId(product_id)
    product = mongo.db.products.find_one({'_id': product_oid})
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    mongo.db.products.update_one({'_id': product_oid}, {'$set': updated_product})
    return jsonify({'message': 'Product data updated'}), 200

@app.route('/product/<product_id>', methods=['GET'])
def get_product_details(product_id):
    # Convert product_id to ObjectId
    product_oid = ObjectId(product_id)
    # Find the product by ID
    product = mongo.db.products.find_one({'_id': product_oid})
    if product:
        # Return product details
        return jsonify({
            '_id': str(product['_id']),
            'name': product['name'],
            'unit_price': product['unit_price'],
            'stock': product['stock'],
        }), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Route delete product
@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Convert product_id to ObjectId
    product_oid = ObjectId(product_id)
    # Find the product by ID
    product = mongo.db.products.find_one({'_id': product_oid})
    if product:
        # Delete the product
        mongo.db.products.delete_one({'_id': product_oid})
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404
# End product API



# Route to create a new sale
@app.route('/sale', methods=['POST'])
def add_sale():
    customer_id = request.json['customer_id']
    product_id = request.json['product_id']
    unit_price = request.json['unit_price']
    qty = request.json['qty']
    total_price = unit_price * qty
    new_sale = {'customer_id': customer_id, 'product_id': product_id, 'unit_price': unit_price, 'qty': qty, 'total_price': total_price}
    sale_id = sales.insert_one(new_sale)
    response = {
        "message": "Sale successfully created",
        "sale_id": str(sale_id.inserted_id)
    }
    return jsonify(response), 201

# Route to retrieve all sales
@app.route('/sale', methods=['GET'])
def get_sales():
    all_sales = sales.find()
    output = []
    for sale in all_sales:
        output.append({'_id' : str(sale['_id']),'customer_id': str(sale['customer_id']), 'product_id': str(sale['product_id']), 'unit_price': sale['unit_price'], 'qty': sale['qty'], 'total_price': sale['total_price']})
    return jsonify({'sales': output}), 200


@app.route('/sale/<sale_id>', methods=['GET'])
def get_sale_details(sale_id):
    # Convert sale_id to ObjectId
    sale_oid = ObjectId(sale_id)
    # Find the sale by ID
    sale = mongo.db.sales.find_one({'_id': sale_oid})
    if sale:
        # Return sale details
        return jsonify({
            '_id': str(sale['_id']),
            'customer_id': str(sale['customer_id']),
            'product_id': str(sale['product_id']),
            'qty': sale['qty'],
            'unit_price': sale['unit_price'],
            'total_price': sale['total_price'],
        }), 200
    else:
        return jsonify({'error': 'Sale not found'}), 404


# Route to update sale
@app.route('/sale/<sale_id>', methods=['PUT'])
def update_sale(sale_id):
    request_data = request.get_json()
    updated_sale = {}
    for field in ['customer_id', 'product_id', 'qty', 'unit_price']:
        if field in request_data:
            updated_sale[field] = request_data[field]

    # Calculate total_price based on qty and unit_price
    updated_sale['total_price'] = updated_sale.get('qty', 0) * updated_sale.get('unit_price', 0)

    sale_oid = ObjectId(sale_id)
    sale = mongo.db.sales.find_one({'_id': sale_oid})
    if not sale:
        return jsonify({'error': 'Sale not found'}), 404
    mongo.db.sales.update_one({'_id': sale_oid}, {'$set': updated_sale})
    return jsonify({'message': 'Sale data updated'}), 200


# Route delete sale
@app.route('/sale/<sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    # Convert sale_id to ObjectId
    sale_oid = ObjectId(sale_id)
    # Find the sale by ID
    sale = mongo.db.sales.find_one({'_id': sale_oid})
    if sale:
        # Delete the sale
        mongo.db.sales.delete_one({'_id': sale_oid})
        return jsonify({'message': 'Sale deleted successfully'}), 200
    else:
        return jsonify({'error': 'Sale not found'}), 404
# End sale API


if __name__ == '__main__':
    app.run(debug=True)
