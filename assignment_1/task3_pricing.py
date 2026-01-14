def task3():
    price_dict = {
        "Laptop": 55000,
        "Phone": 30000,
        "Headphones": 2000,
        "Keyboard": 1500,
        "Mouse": 800,
        "Monitor": 12000
    }

    price_dict["Tablet"] = 18000
    price_dict["Phone"] = 32000

    product_to_remove = "Camera"
    if product_to_remove in price_dict:
        del price_dict[product_to_remove]

    total = 0
    for price in price_dict.values():
        total += price

    avg = total / len(price_dict)
    print("Average price:", avg)

    max_product = max(price_dict, key=price_dict.get)
    min_product = min(price_dict, key=price_dict.get)

    print("Max price product:", max_product)
    print("Min price product:", min_product)
