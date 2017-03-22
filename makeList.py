#[x*x for x in range(1, 11) if not(x*x%2)]

listA = []

for x in range(1, 11):
    if not(x*x%2):
        listA.append(x*x)

print(listA)
