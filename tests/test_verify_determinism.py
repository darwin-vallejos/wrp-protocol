from witness.verify import verify_receipt
import json
import tempfile
import os

def test_verify_accepts_valid_receipt():
    receipt = {
        "payload": {
            "decision": "ALLOW",
            "trust_score_bp": 88333,
            "amount_cents": 0
        },
        "receipt_hash": "dummy"
    }

    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as f:
        json.dump(receipt, f)
        path = f.name

    try:
        # Should not throw
        verify_receipt(path)
    finally:
        os.unlink(path)
