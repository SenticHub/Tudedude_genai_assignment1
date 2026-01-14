def task2():
    categories = [
        "Electronics", "Electronics", "Accessories",
        "Accessories", "Accessories", "Electronics"
    ]

    categories_set = set(categories)

    categories_set.add("Gaming")
    categories_set.add("Electronics")

    print("Categories:", categories_set)
    print("Is Electronics present?", "Electronics" in categories_set)
    print("Total unique categories:", len(categories_set))
