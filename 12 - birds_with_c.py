# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]
new_birds = []

for bird in birds:
    if bird.lower().startswith("c"):
        new_birds.append(bird)

print(birds)
print(new_birds)
