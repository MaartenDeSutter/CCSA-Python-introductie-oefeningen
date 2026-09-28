getallen = []
for i in range(3):
    getallen.append(int(input()))
getallenReversed = getallen[::-1]
output = ''
for getal in getallenReversed:
    output = output + (f"{getal} ")
print(output)