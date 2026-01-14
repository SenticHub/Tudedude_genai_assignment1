def task4():
    products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]
    categories = ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics"]

    price_dict = {
        "Laptop": 55000,
        "Phone": 32000,
        "Headphones": 2000,
        "Keyboard": 1500,
        "Mouse": 800,
        "Monitor": 12000
    }

    catalog = []
    for i in range(len(products)):
        catalog.append((products[i], price_dict[products[i]], categories[i]))

    category_to_products = {}
    for item in catalog:
        product, price, category = item
        if category not in category_to_products:
            category_to_products[category] = []
        category_to_products[category].append(product)

    max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

    print("Category with max products:", max_category)
    print("Products:", category_to_products[max_category])
