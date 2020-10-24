guest_list = ["jesus", "bogart", "deming"]
print(guest_list)

print(guest_list[1].title() + ", Can't make it!")

del guest_list[1]
print(guest_list)

guest_list.append("bernie mac")
print(guest_list)


print("You, " + guest_list[0].title() + " are invited.")
print("You, " + guest_list[1].title() + " are invited.")
print("You, " + guest_list[2].title() + " are invited.")


guest_list.insert(0, "joseph")
guest_list.insert(2, "judas")
guest_list.append(" michael jackson")

print("You, " + guest_list[0].title() + " are invited.")
print("You, " + guest_list[1].title() + " are invited.")
print("You, " + guest_list[2].title() + " are invited.")
print("You, " + guest_list[3].title() + " are invited.")
print("You, " + guest_list[4].title() + " are invited.")
print("You, " + guest_list[-2].title() + " are invited.")
print("You, " + guest_list[-1].title() + " are invited.")

print("I can only invite 2 poeple for dinner, sorry.")

pop_guest = guest_list.pop()
print(pop_guest)

print(" I am sorry " + pop_guest.title() + ".")

pop_guest = guest_list.pop()
print(pop_guest)
print(" I am sorry " + pop_guest.title() + ".")

pop_guest = guest_list.pop()
print(pop_guest)
print(" I am sorry " + pop_guest.title() + ".")

pop_guest = guest_list.pop()
print(pop_guest)
print(" I am sorry " + pop_guest.title() + ".")

print(guest_list)

print("Good news " + guest_list[1].title() + " ,the dinner is still on.")
print("Good news " + guest_list[0].title() + " ,the dinner is still on.")

del guest_list[0]
del guest_list[0]

print(guest_list)


print(len(guest_list))