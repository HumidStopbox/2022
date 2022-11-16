import os

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir, "the-input.txt"))
lines = f.readlines()
for line in lines:
    print(f"{line.strip()}")
words = line.split(" ")
print(f"lines: {len(lines)}")
f.close()
print("I couldn't figure out how to make it say 'words: _' so instead i did lines")