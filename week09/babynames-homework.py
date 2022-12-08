import os

sourceDir = os.path.dirname(__file__)
filePath =  os.path.join(sourceDir, "Popular_Baby_Names.csv")
f = open(filePath)

#ignore the heading Line
f.readline()



names = set()
for line in f:
    data =  line.strip().split(",")
    names.add(data[3])
    print(f"names: {names}")
f.close()
print("I tried hard but never was able to figure out how to sort the names from A-Z")