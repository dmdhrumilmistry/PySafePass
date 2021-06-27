import hashlib

def hashdata(data:str):
    data = data.encode('utf-8')
    hashed_data = hashlib.md5(data).hexdigest()
    return hashed_data


