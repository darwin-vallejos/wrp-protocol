import json
import hashlib
import sys
from wrp_protocol.canonical import canonical_bytes

def verify_receipt(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    payload = receipt.get("payload")
    expected = receipt.get("receipt_hash")

    if payload is None or expected is None:
        raise ValueError("Invalid receipt format")

    computed = hashlib.sha256(canonical_bytes(payload)).hexdigest()

    if computed != expected:
        raise ValueError("Receipt verification FAILED")

    print("Receipt verification OK")

def main():
    if len(sys.argv) != 2:
        print("Usage: wrp <receipt.json>")
        sys.exit(1)

    verify_receipt(sys.argv[1])

if __name__ == "__main__":
    main()
