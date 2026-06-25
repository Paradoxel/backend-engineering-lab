products = [
{"name": "Laptop", "price": 1000},
{"name": "Keyboard", "price": 50},
{"name": "Mouse", "price": 20},
]

class QuerySet:
    def __init__(self, data):
        self.data = data


# Simulates:
# Product.objects.all()
    def all(self):
        return QuerySet(self.data)

# Simulates:
# Product.objects.count()   
    def count(self):
        return len(self.data)

# Simulates:
# Product.objects.first()
    def first(self):
        return self.data[0]

# Simulates:
# Product.objects.filter(price=...)
    def filter_by_price(self, price):
        result = []

        for product in self.data:
            if product["price"] == price:
                result.append(product)

        return QuerySet(result)

# Makes printing easier
    def __repr__(self):
        return f"QuerySet({self.data})"


queryset = QuerySet(products)

print(queryset.all())
print(queryset.count())
print(queryset.first())
print(queryset.filter_by_price(20).count())
print(queryset.filter_by_price(20))
