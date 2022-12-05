guests = open("guests.txt", "w")
initial_guests = ["Bod", "Manuel", "Andrena", "Polly"]

for i in initial_guests:
    guests.write(i + '\n')
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line.strip().upper())