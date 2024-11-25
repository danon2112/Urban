
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a')
        file.write('')
        file.close()


    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text


    def add(self, *products):
        for i in range(len(products)):
            product = products[i].split(',')
            if products[i] in self.get_products():
                print(f'Продукт {product[0]} уже есть в магазине.')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{products[i]}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(str(p1), str(p2), str(p3))

print(s1.get_products())
