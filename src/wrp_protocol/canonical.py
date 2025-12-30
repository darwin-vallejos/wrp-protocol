import json

def canonical_bytes(obj) -> bytes:
    """
    Deterministic JSON canonicalization:
    - UTF-8
    - sorted keys
    - no whitespace
    """
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
