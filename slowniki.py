empty_d = dict()
print(type(empty_d))

d = {"k": "v", "k1": "v1", "k2": "v2", "k3": "v3"}


print(d)

d["k4"] = "v4"
print(d)

del d["k4"]
print(d.get("k4"))

d.pop("k3")
print(d.get("k3"))

print(d.keys())
print(d.values())
print(d.items())

# 'k' : 'v' -> item

d1 = {2: "Test", 1: "Test", 0: "Test"}

print(sorted(d1.items()))  # tylko tutaj, ta zmiana sie nie zapisuje
print(d1)
