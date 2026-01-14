def task1():
    products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]

    sample_product = ("Laptop", 55000, "Electronics")

    print("Second product:", products[1])
    print("Last product:", products[-1])

    products.append("Tablet")
    products.append("Printer")
    print("Updated products:", products)

    temp = list(sample_product)
    temp[1] = 52000
    sample_product = tuple(temp)
    print("Updated sample product:", sample_product)
