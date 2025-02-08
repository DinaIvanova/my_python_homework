purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def group_by_category(purchases): # Вспомогательная функция группировка по категориям
    categories_dict = {}
    for purchase in purchases:
        category = purchase["category"]
        categories_dict[category] = categories_dict.get(category, [])
    return categories_dict

def total_revenue(purchases): #Общая выручка (цена * количество для всех записей)
    total = sum(purchase['price'] * purchase['quantity'] for purchase in purchases)
    return total

def items_by_category(purchases): #Список товаров по категориям.
    category_items = group_by_category(purchases)
    for purchase in purchases:
        category = purchase["category"]
        if purchase["item"] not in category_items[category]:
            category_items[category].append(purchase["item"])
    return category_items

def expensive_purchases(purchases, min_price): #Список покупок, где цена превышает заданное значение.
    expensive_purchases_list = []
    for purchase in purchases:
        if purchase["price"] >= min_price:
            expensive_purchases_list.append(purchase)
    return expensive_purchases_list

def average_price_by_category(purchases): #Средняя цена товаров по категориям.
    average_price_dict = group_by_category(purchases)
    for purchase in purchases:
        category = purchase["category"]
        average_price_dict[category].append(purchase["price"])
    for key, value in average_price_dict.items():
        average_price_dict[key] = sum(value) / len(value)
    return average_price_dict

def most_frequent_category(purchases): #Категория с наибольшим числом проданных товаров.
    category_counts = {}
    for purchase in purchases:
        category = purchase["category"]
        quantity = purchase["quantity"]
        category_counts[category] = category_counts.get(category, 0) + quantity
    most_frequent = max(category_counts, key=category_counts.get)
    return most_frequent

min_price = 1.0

print(f'Общая выручка: {total_revenue(purchases)}')
print(f'Товары по категориям: {items_by_category(purchases)}')
print(f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')