class book():
    def __init__(self):
        self.cook_book = {}
        self.shop_list = {}

    def read(self):
        with open('cook_book.txt', encoding='utf-8') as file:
            last_key = ''
            for line in file:
                line = line.strip()
                if line.isdigit():
                    continue
                elif line and '|' not in line:
                    self.cook_book[line] = []
                    last_key = line
                elif line and '|' in line:
                    name, qt, msure = line.split(" | ")
                    self.cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))

    def shop(self,dishes, person_count):
        for dish in dishes:
            if dish in self.cook_book:
                for el in self.cook_book[dish]:
                    if el['ingredient_name'] not in self.shop_list:
                        self.shop_list[el['ingredient_name']]={'measure':el['measure'],'quantity':el['quantity']*person_count}
                    else:
                        self.shop_list[el['ingredient_name']]['quantity'] +=el['quantity'*person_count]




book1=book()
book1.read()
book1.shop(['Запеченный картофель', 'Омлет'], 2)
print(book1.cook_book)
print(book1.shop_list)
