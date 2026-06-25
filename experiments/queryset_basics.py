# Sample Data (simulating database records)

products = [
{"name": "Laptop", "price": 1000},
{"name": "Keyboard", "price": 50},
{"name": "Mouse", "price": 20},
]

# Django Equivalent:

# Product.objects.all()

def all_product():
    return products

print(all_product())

# Django Equivalent:

# Product.objects.filter(price=20)

def filter_by_price(price):
    result = []


    for product in products:
        if product["price"] == price:
            result.append(product)

    return result


print(filter_by_price(20))

# Django Equivalent:

# Product.objects.count()

def count_products():
    return len(products)

print(count_products())

# Django Equivalent:

# Product.objects.filter(...).exists()

def exists_products(product):
    return products.__contains__(product)

print(exists_products({"name": "Mouse", "price": 20}))

# Django Equivalent:

# Product.objects.first()

def first_product():
    return products[0]

print(first_product())
