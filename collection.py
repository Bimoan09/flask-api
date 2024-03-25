from pymongo import MongoClient

# Koneksi ke MongoDB Server
client = MongoClient('mongodb://localhost:27017/')

# Pilih database
db = client['penjualan']

# Buat collection Customer
customers_collection = db['customers']

# Buat collection Product
products_collection = db['products']

# Buat collection Sales
sales_collection = db['sales']

# Struktur field untuk Customer
customer_data = {
        "name": "Ahmad Dhani", # Char
        "handphone": "0812345678" # Char
    }


# Struktur field untuk Product
product_data = {
    "name": "Produk 1", #Char
    "unit_price": 150000.0,  # Float
    "stock": 100  # Integer
}

# Struktur field untuk Sales
sales_data = {
    "customer_id": None,  # Integer
    "product_id": None,  # Integer
    "unit_price": 200000.0,  # Float
    "qty": 50,  # Integer
    "total_price": 400000.0  # Float
}

# Insert data ke collection Customer
customer_id = customers_collection.insert_one(customer_data).inserted_id

# Insert data ke collection Product
product_id = products_collection.insert_one(product_data).inserted_id

# Mengisi field customer_id dan product_id dalam data Sales
sales_data["customer_id"] = customer_id
sales_data["product_id"] = product_id

# Insert data ke collection Sales
sales_collection.insert_one(sales_data)

# Menutup koneksi
client.close()
