import sys
from src.verify_receipt import verify_receipt

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify.py <receipt.json>")
        sys.exit(1)

    verify_receipt(sys.argv[1])
