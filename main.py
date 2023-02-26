from pprint import pprint



def read_file():
	with open('recipe.txt', encoding='UTF-8') as file:
		cook_book = {}
		for line in file:
			dishes_name = line.strip()
			# print(dishes_name)
			food_count = int(file.readline())
			food_list = []
			for element in range(food_count):
				numbers = file.readline().strip()
				ingredient_name, quantity, measure = numbers.split(' | ')
				food_list.append({
					'ingredient_name': ingredient_name,
					'quantity': int(quantity),
					'measure': measure})
			cook_book[dishes_name] = food_list
			file.readline()
	return cook_book


def get_shop_list_by_dishes(dishes, person_count):
	cook_book = read_file()
	dishes_list = {}
	for dish in dishes:
		for element in cook_book[dish]:
			if element['ingredient_name'] not in dishes_list:
				dishes_list[element['ingredient_name']] = {'measure': element['measure'],
														   'quantity': element['quantity'] * person_count}
			else:
				dishes_list[element['ingredient_name']]['quantity'] += element['quantity'] * person_count
	return dishes_list


print('----- Задача №1 -----')
print()
pprint(read_file())
print()
print('----- Задача №2 -----')
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Запеченный'], 9), width=100)




