hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


def hotel_list(hotels):
    result = ""
    for i in hotels:
        result = result + i["name"] +","
    return result[:-1]

def avg_price(hotels):
    result = 0 
    count = 0 
    for i in hotels:
        result = result + i["price"]
        count = count + 1 
    return int(result / count)

def cheaper():
    if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
        return "Kraków"
    else:
        return "Sopot"

print(hotel_list(hotels_in_Krakow))
print(avg_price(hotels_in_Krakow))
print(hotel_list(hotels_in_Sopot))
print(avg_price(hotels_in_Sopot))
print(cheaper())
