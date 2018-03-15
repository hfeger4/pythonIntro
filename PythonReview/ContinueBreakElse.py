shopping_list = ["milk", "eggs", "pasta", "awd", "bread","rice"]

# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

nasty_food_item = ""
for item in shopping_list:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that then please.")

if nasty_food_item == 'spam':
    print("Can't i have something without spam?")