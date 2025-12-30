import json
import hashlib
from src.canonical import canonical_bytes

with open("test_receipt.json", "r", encoding="utf-8") as f:
    r = json.load(f)

h = hashlib.sha256(canonical_bytes(r["payload"])).hexdigest()
r["receipt_hash"] = h

with open("test_receipt.json", "w", encoding="utf-8") as f:
    json.dump(r, f, indent=2)

print("hash generated:", h)
