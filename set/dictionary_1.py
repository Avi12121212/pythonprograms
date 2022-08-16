d = {}
d1 = {"herry": "burgar", "harsh": "roti", "shubham": {"b": "egg", "l": "rice", "d": "meat"}}
# print(d1["shubham"])

d = {1: "one", 2: "two"}
# print(d)
d[3] = "three"
# print(d)
d[3] = "3-three"
print(d)

print("(d.items)")
for key, value in d.items():
    print(value, ",", key)
print("(key)")
for key in d.keys():
    print(key)
print("(value)")
for value in d.values():
    print(value)

    # Searching
    # for values.get method returns None if value is not found
key = d.get(2)
print(key)

# we can also search by direct indexing it can throws exception if not found
print(d[2])
print(d[3])
print(d[1])

# we can remove items from dictionary

# d.pop(2)
print(d)

d.popitem()  # removw the last elememnt
d.popitem()
d.popitem()
print(d)

runs = [1, 10, 23, 34, 56]
names = ["Sachin", "Rahul", "Mahender", "Sourav", "zaheer"]

zipdictionary = zip(names, runs)
zipdictionary = list(zipdictionary)

print("zip ", zipdictionary)



newdick1 = {name: run for (name, run) in zip(names, runs)}
print(newdick1)
newdick2 = {run: name for (run, name) in zip(runs, names)}
print(newdick2)

newdict3 = {run: name for (run, name) in zip(runs, [run * 2 for run in runs])}
print(newdict3)

newdict4 = {run: name for (run, name) in zip(runs, [(lambda run: run + 2)(run) for run in runs])}
print(newdict4)

newdict5 = dict.fromkeys(runs)
print(newdict5)
