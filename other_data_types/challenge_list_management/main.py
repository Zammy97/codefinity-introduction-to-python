meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
#combined list
deli_dept = [meat, cheese]
print(deli_dept)
if meat[2] < 100:
    meat[2] = 100
    
print("Initial Deli List:", deli_dept)

deli_dept.sort()
print("Updated Deli List:", deli_dept)