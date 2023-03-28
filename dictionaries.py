configuratie = {
    "processor": "Intel i7 Keylane",
    "memory": "16GB Kingston",
    "ssd": "512GB"
}

print(configuratie["processor"])

configuratie.update({"processor": "Intel Core i7"})

print(configuratie.get("processor"))

print(configuratie)
print(configuratie.keys())
print(configuratie.values())
print(configuratie.items())