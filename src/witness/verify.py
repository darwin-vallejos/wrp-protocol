import json
import hashlib

def canonical(obj):
    return json.dumps(
        obj,
        separators=(",", ":"),
        sort_keys=True,
        ensure_ascii=False,
    )

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def verify_receipt(path: str) -> None:
    # Load receipt safely (UTF-8 + BOM tolerant)
    with open(path, "r", encoding="utf-8-sig") as f:
        receipt = json.load(f)

    payload = receipt["payload"]
    claimed_hash = receipt["receipt_hash"]

    computed = sha256_hex(canonical(payload))

    print(f"Computed: {computed}")
    print(f"Claimed:  {claimed_hash}")
    print(f"MATCH:    {computed == claimed_hash}")
