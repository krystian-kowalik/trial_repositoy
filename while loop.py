i1 = 1
while i1 <= 10:
    print(i1, end="\t")
    i1 += 1

print("\nSkończyłem z pętlą")

closeProgram = False

i=1
while closeProgram == False:
    print(i, "^3=", i**3)
    name = input("Kończymy? (y/n)")
    if name == "y":
        closeProgram = True
    i=i+1
