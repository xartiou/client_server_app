# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.

import json

# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
def write_order_to_json(item, quantity, price, buyer, date) -> None:
    json_key = 'orders'
    file_link = 'orders.json'
    encoding = 'utf-8'
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    # Функция должна предусматривать запись данных в виде словаря в файл orders.json.
    # При записи данных указать величину отступа в 4 пробельных символа
    with open(file_link, encoding=encoding) as f:
        json_dict = json.load(f)

    with open(file_link, 'w', encoding=encoding) as f:
        json_dict[json_key].append(order)
        json.dump(json_dict, f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    write_order_to_json('Cheburashka', 1, 1560.00, 'Krokodil Gena', '28.02.2022')