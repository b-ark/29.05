# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

# Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# сделал функцию доступной для словарей, где ключи идут не в одном порядке,
# для этого сделал преребор значений по всему словарю
def total_price(dict1, dict2):
    result = 0
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                result += dict1[key1] * dict2[key2]
    return result


# это подходит только для наших словарей, так как в них ключи идут в одинаковом порядке
def lazy_total_price(dict1, dict2):
    result = 0
    for key, value in dict1.items():
        result += dict1[key] * dict2[key]
    return result


print(f'Total price of the stock is {total_price(stock, prices)}')
print(f'Total price of the stock is {lazy_total_price(stock, prices)}')
