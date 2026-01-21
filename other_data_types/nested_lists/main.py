vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()

print("Updated Vegetable Inventory:", vegetables)
if "carrots" == vegetables:
    print("Carrots are already in the list")
if "cucumbers" == vegetables:
    print("Cucumbers are already in the list")