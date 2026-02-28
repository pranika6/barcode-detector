import json
import os
def load_barcodes(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return {}

    with open(filename, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Error: Failed to parse JSON.")
            return {}

def verify_barcode(barcodes, barcode):
    product = barcodes.get(barcode)
    if product:
        print("\n=== Product Information ===")
        print(f"Name: {product['name']}")
        print(f"Brand: {product['brand']}")
        status = product['status']
        if status == 'genuine':
            print("✅ Status: Genuine Product")
        elif status == 'fake':
            print("❌ Status: Fake Product")
        else:
            print("⚠️ Status: Unknown")
    else:
        print("⚠️ Barcode not found in database.")

def main():
    print("=== Barcode Verifier ===")
    barcodes = load_barcodes('barcodes.json')

    if not barcodes:
        return

    while True:
        code = input("\nEnter a barcode (or type 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            print("Exiting program.")
            break
        verify_barcode(barcodes, code)

# ✅ THIS LINE MUST HAVE DOUBLE UNDERSCORES
if __name__ == '__main__':
    main()