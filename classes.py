
import json
import os
CWD = os.path.dirname(__file__)


class BarProduct: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def to_dict(self):
            result = {
                "name": self.name,
                "price": self.price
                }
            return result

    def __str__(self):
     return "Product: " + self.name + " Price: " + str(self.price)



class Bill:
    def __init__(self, id):
        self.id = id
        self.consum_products = []

    def final_bill(self):
        total = 0
        for p in self.consum_products:
            total = total + p.price
        return f"The total of your bill: {total} EUR\n\n"

    def add_product(self, name, price):
        a = BarProduct(name, price)
        self.consum_products.append(a)

    def to_dict(self):
            result = {
                "id": self.id,
                "consum_products": json.dumps(self.consum_products, default=BarProduct.to_dict)
                } 
            return result

    def __str__(self):
        output = f"Bill:\n ID: {str(self.id)}\n"
        for p in self.consum_products:
            output = output + p.__str__()+"\n"
        return output

