import hashlib
import json

def hash_dict(d: dict):
    hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()