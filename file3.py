import json

# 1. Read existing JSON
with open('dummy.json', 'r') as f:
    data = json.load(f)

# 2. New user
new = {
    "id": 45,
    "name": "Alice",
    "age": 24,
    "email": "alice@example.com",
    "is_active": True,
    "scores": [78, 85, 90]
}

# 3. Append to users list
data["users"].append(new)

# 4. Write back to file (overwrite)
with open('dummy.json', 'w') as f:
    json.dump(data, f, indent=4)

print("User added successfully ✅")
