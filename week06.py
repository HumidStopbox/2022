names = ("dogs", "cats", "rabbits", "cows", "horses", "sea otters")
numbers = []
numbers.append(float(input(f"How many {names[0]}? ")))
numbers.append(float(input(f"How many {names[1]}? ")))
numbers.append(float(input(f"How many {names[2]}? ")))
numbers.append(float(input(f"How many {names[3]}? ")))
numbers.append(float(input(f"How many {names[4]}? ")))
numbers.append(float(input(f"How many {names[5]}? ")))

min = numbers[0]
max = numbers[0]

if numbers[1] < min:
    min = numbers[1]
if numbers[1] > max:
    max = numbers[1]

if numbers[2] < min:
    min = numbers[2]
if numbers[2] > max:
    max = numbers[2]

if numbers[3] < min:
    min = numbers[3]
if numbers[3] > max:
    max = numbers[3]

if numbers[4] < min:
    min = numbers[4]
if numbers[4] > max:
    max = numbers[4]

if numbers[5] < min:
    min = numbers[5]
if numbers[5] > max:
    max = numbers[5]

print(f"Minimum: {min}")
print(f"Minimum: {max}")

answer = input( "A sea otter is my favorit animal. What's your favorite animal? ")
if answer == [5]:
    print("Great Choice!")
else:
    print("Great Choice!")