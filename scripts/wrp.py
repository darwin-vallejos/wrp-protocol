import json
import hashlib
import sys

from wrp_protocol.canonical import canonical_bytes


def verify_receipt(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        receipt = json.load(f)

    if "payload" not in receipt:
        raise ValueError("Missing payload")

    if "receipt_hash" not in receipt:
        raise ValueError("Missing receipt_hash")

    payload = receipt["payload"]
    expected_hash = receipt["receipt_hash"]

    canonical = canonical_bytes(payload)
    actual_hash = hashlib.sha256(canonical).hexdigest()

    if actual_hash != expected_hash:
        raise ValueError("Receipt hash mismatch")

    print("OK: receipt verified")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: wrp <receipt.json>")
        sys.exit(1)

    verify_receipt(sys.argv[1])


if __name__ == "__main__":
    main()
