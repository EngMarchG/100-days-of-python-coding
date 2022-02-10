fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code works without crashes
def make_pie(index):

    fruit = fruits[index]
    print(fruit + " pie")

make_pie(4)
































fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code works without crashes
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Oops your number is out of index")
    else:
        print(fruit + " pie")

make_pie(4)