import uuid

def generate_uuids(n):
    return [str(uuid.uuid4()) for _ in range(n)]

# Example: Generate 5 UUIDs and print each one on a new line
n = 5
uuid_list = generate_uuids(n)

for u in uuid_list:
    print(u)
