
def read_file(file):
    names = []
    size = []
    cont = 0
    with open(file, 'r') as arq:
        for line in arq:
            parts = line.split()

            name = parts[0]
            names.append(name)

            number = float(parts[1])
            size.append(number)

            cont += 1
    return names, size, cont


def calculate(cont, size):
    total = 0
    for i in range(cont):
        size[i] = (size[i]/1024)/1024
        total += size[i]
    return size, total


def calculate_pct(cont, size, total):
    pct = []
    x = 0
    for i in range(cont):
        x = (size[i] / total * 100)
        pct.append(x)
    return pct


def main():
    arq = 'users.txt'
    names, size, cont = read_file(arq)
    size, total = calculate(cont, size)
    size_pct = calculate_pct(cont, size, total)
    for i in range(cont):  # testing
        print(i+1, f"{names[i]} {size[i]:.2f} MB {size_pct[i]:.2f}%")


main()
