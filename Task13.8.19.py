n = int(input("How many tickets are required?\n"))
s = 0
for i in range(n):
    age = int(input("Visitor's age:\n"))
    if age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390
if n > 3:
    s = s*0.9
print("Total -", s)
