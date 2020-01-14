# 1. Create an empty set named showroom.

# 2. Add four of your favorite car model names to the set.
showroom = {"rx8", "miata", "ioniq", "elantra"}
# 3. Print the length of your set.
print(showroom)
# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("rx8")
# 5. Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
# 6. Using update(), add two more car models to your showroom with another set.
more_cars = {"accord", "ranger"}
showroom.update(more_cars)
print(showroom)
# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("ranger")
print(showroom)


# 1. Now create another set of cars in a variable junkyard.
# Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"ranger", "rx8", "accord", "maxima"}
# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
intersec = showroom.intersection(junkyard)
print(intersec)
# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroomAndJunkyard = showroom.union(junkyard)
print(showroomAndJunkyard)
# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroomAndJunkyard.discard("maxima")
print(showroomAndJunkyard)