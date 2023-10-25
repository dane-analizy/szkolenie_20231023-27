zmienna = "linia 2"
with open("dane_oczyszczone.csv", 'w') as f:
    f.write("linia 1\n")
    f.write(f"{zmienna}\n")


# f = open(...)
# # kolejne instruncje
# f.close()
