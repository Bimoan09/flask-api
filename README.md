i assuming you have installed Python3, Flask and MongoDb in your environment, next:

i am using ubuntu 20.04 in my Local Laptop,

1. git clone this repository
2. open **Terminal** ubuntu and activate VirtualENV python
3. go to your Path
4. RUN **python3 collection.py** for create Collection in mongoDB
5. RUN **python3 api.py** for RUNNING Flask server in your local Development server or your local laptop
6. open API testing tools like **Postman** or API tetsing tools you prefer, testing bellow Endpoint :

Customers Endpoint:
1. localhost:5000/customer - POST - POST customers
2. localhost:5000/customers - GET - All customers
3. localhost:5000/customer/<customer_id> - GET - Details customers with ID
4. localhost:5000/customer/<customer_id> - PUT - Update customers
5. localhost:5000/customer/<customer_id> - DELETE - Delete customers

Products Endpoint:
1. localhost:5000/product - POST - POST product
2. localhost:5000/products - GET - All products
3. localhost:5000/product/<product_id> - GET - Details product with ID
4. localhost:5000/product/<product_id> - PUT - Update product
5. localhost:5000/product/<product_id> - DELETE - Delete product


Sale Endpoint:
1. localhost:5000/sale - POST - POST sale
2. localhost:5000/sale - GET - All Sale
3. localhost:5000/sale/<sale_id> - GET - Details sale with ID
4. localhost:5000/sale/<sale_id> - PUT - Update sale
5. localhost:5000/sale/<sale_id> - DELETE - Delete sale
