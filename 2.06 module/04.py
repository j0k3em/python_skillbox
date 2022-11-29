goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_object in goods:
    for i_store in store.keys():
        if i_store == goods[i_object]:
            count_product = 0
            price_product = 0
            for price in store[i_store]:
                count_product += price.get('quantity')
                price_product += price.get('price')
            print(f"{i_object} - {count_product}, стоимость {count_product * price_product} руб")