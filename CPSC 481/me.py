firstName = "Joshua"
lastName = "Castaneda"
fullName = f"{firstName} {lastName}"

print(fullName)

newName = input("What is your name: ").lower()

print(f"Whats up {newName.title()}? damn you cute as hell")

favoriteThings = ["stuff", "tings", "and stuff", 1, 2, 3, 4, 5]

newFavoriteThing = input("Whats your favorite thing? ")

 
favoriteThings.append(newFavoriteThing)

print(favoriteThings)

firstThing = favoriteThings.pop(0)



print(favoriteThings)

print(firstThing)

for thing in favoriteThings:
    print(thing)

numbers = list(range(10))
print(numbers)