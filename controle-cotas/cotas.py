
def read_file(file):
    names = []
    numbers = []
    cont = 0
    with open(file, 'r') as arq:
        for line in arq:
            parts = line.split()

            name = parts[0]
            names.append(name)

            number = float(parts[1])
            numbers.append(number)

            cont += 1
    return names, numbers, cont


def calculate(cont, numbers):
    total = 0
    for i in range(cont):
        numbers[i] = (numbers[i]/1024)/1024
        total += numbers[i]
    return numbers, total


def main():
    arq = 'users.txt'
    names, numbers, cont = read_file(arq)
    numbers, total = calculate(cont, numbers)
    for i in range(cont):  # testing
        print(i+1, f"{names[i]} {numbers[i]:.2f}")


main()
