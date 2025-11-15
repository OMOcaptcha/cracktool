import hashlib
with open(__file__, "rb") as f:
    data = f.read()

current = hashlib.sha256(data).hexdigest()
print(current)
