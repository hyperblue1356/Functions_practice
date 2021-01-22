fruit = {"orange": " An orange fruit",
         "apple": "A red fruit",
         "blapple": "A made up fruit",
         "conaple": "An even more made up fruit"}

print(fruit)
print("-" * 40)
print(fruit.items())
print("-" * 40)
f_tuple = tuple(fruit.items())
print(f_tuple)
print("-" * 40)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
    print("-" * 40)

print(dict(f_tuple))
print("-" * 40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + "-" + fruit[f])

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + "-" + fruit[f])

# print(fruit.keys())
# print()
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)
# print("-" *40)
#
# fruit["tomatoe"] = "not nice"
# print(fruit_keys)



# # print(fruit["blapple"])
#
# while True:
#     dict_key = input("please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "we don't have a " + dict_key)
#     # print(description)
#     if dict_key in fruit:
#             description = fruit.get(dict_key)
#             print(description)
#     else:
#         print("we don't have a " +dict_key)