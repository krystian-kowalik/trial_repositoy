i = 1
while i <= 10:
    print(i, end="\t")
    i += 1

print("\nSkończyłem z pętlą")

closeProgram = False

i=1
while closeProgram == False:
    print(i, "^3=", i**3)
    name = input("Kończymy? (y/n)")
    if name == "y":
        closeProgram = True
    i=i+1
