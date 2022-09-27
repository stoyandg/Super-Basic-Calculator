chislo1 = int(input("Molq vavedete chislo!"))
operacia = input("!sabirane ili !izvajdane")
chislo2 = int(input("Molq vavedete chislo!"))

if operacia == "!sabirane":
    rezultat = int(chislo1) + int(chislo2)
    print("Vashiqt rezultat e:", rezultat)
elif operacia == "!izvajdane":
    rezultat = int(chislo1) - int(chislo2)
    print("Vashiqt rezultat e: ", rezultat)



