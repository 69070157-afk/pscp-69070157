'eee'
def main():
    'eee'
    material = [
    'Pad Thai Sauce',
    'Tofu',
    'Pickle Turnip',
    'Shrimp',
    'Bean Sprouts',
    'Noodle',
    'Chives',
    'Lime',
    'Egg',
    'Oil',
    'Peanuts'
    ]
    not_have = material.copy()
    flavor = [
    'Sweet',
    'Sour',
    'Salty'
    ]
    flavor_not_have = flavor.copy()
    while True:
        n = input()
        if n == 'Cook':
            break
        if n not in material:
            print("This is not Pad Thai!!!")
            return
        if n in not_have:
            not_have.remove(n)
    if not_have:
        print("This is bad!")
        return
    while True:
        n = input()
        if n == 'End':
            break
        if n not in flavor:
            print("Not Bad...")
            return
        if n in flavor_not_have:
            flavor_not_have.remove(n)
    if flavor_not_have:
        print("Not Bad...")
        #print(flavor_not_have)
    else:
        print("Delicious!")
main()
