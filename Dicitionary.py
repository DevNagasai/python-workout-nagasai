from typing import OrderedDict


MENU = {'sandwich':10, 'tea':7 , 'salad': 9}

def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip()
        
        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')

        else:
            print(f'We are fresh out of {order} today!')

    print(f'Your total is {total}')


restaurant()


def get_rainfall():
    rainfall = {}
    while True:
        city_name = input("Enter city name: ")
        if not city_name:
            break
        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name,0) +int(mm_rain)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()


def diffdict(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first[key] != second[key]:
            output[key] = [first.get(key), second.get(key)]

    return output

d1 = {'a': 1, 'b': 2 , 'c': 3}
d2 = {'a': 1, 'b':2 , 'c':3}

print(diffdict(first = d1, second = d2))


