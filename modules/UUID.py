import uuid

def uuid_to_decimal():
    uuid_str = str(uuid.uuid4()).replace('-', '')
    uuid_int = int(uuid_str, 16)
    return uuid_int

print(uuid_to_decimal())