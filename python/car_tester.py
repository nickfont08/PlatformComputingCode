from car import Car
cars = []
with open("cars.txt") as file:
    for line in file:
        stripped_line = line.strip()
        tokens = stripped_line.split()
        car1 = Car(tokens[0], tokens[1], int(tokens[2]), int(tokens[3]))
        cars.append(car1)
first = cars[0]
second = cars[1]
second.drive()
print(second)