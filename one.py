"""Simple Billing System - PS No. 33 (Python 3, no external libraries)."""
from datetime import datetime

PRODUCTS = {"rice": 50, "sugar": 40, "oil": 120}
GST_RATE = 0.05
BILL_FILE = "bill.txt"

def display_products():
    print("\nAvailable products:")
    for name, price in PRODUCTS.items():
        print(f"{name.title()}: Rs.{price}")

def add_item(items, name, quantity):
    product = name.strip().lower()
    if product not in PRODUCTS:
        print("Invalid product. Available: Rice, Sugar, Oil")
        return False
    try:
        qty = int(quantity)
    except (ValueError, TypeError):
        qty = 0
    if qty < 1:
        print("Quantity must be at least 1.")
        return False
    amount = PRODUCTS[product] * qty
    items.append({"product": product.title(), "quantity": qty,
                  "unit_price": PRODUCTS[product], "amount": amount})
    print(f"{product.title()} x{qty} added | Amount: {amount}")
    return True

def calculate_totals(items):
    subtotal = sum(item["amount"] for item in items)
    gst = subtotal * GST_RATE
    return subtotal, gst, subtotal + gst

def generate_bill(customer, items):
    subtotal, gst, total = calculate_totals(items)
    lines = [
        "=" * 52,
        "                 SIMPLE BILLING SYSTEM",
        "=" * 52,
        f"Customer: {customer}",
        f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        "-" * 52,
        f"{'Product':<12}{'Qty':>6}{'Rate':>14}{'Amount':>14}",
        "-" * 52
    ]
    for item in items:
        lines.append(f"{item['product']:<12}{item['quantity']:>6}"
                     f"{item['unit_price']:>14.2f}{item['amount']:>14.2f}")
    lines += [
        "-" * 52,
        f"{'Subtotal':>36} Rs. {subtotal:>10.2f}",
        f"{'GST (5%)':>36} Rs. {gst:>10.2f}",
        f"{'Grand Total':>36} Rs. {total:>10.2f}",
        "=" * 52,
        "             Thank you for shopping!",
        "=" * 52
    ]
    return "\n".join(lines)

def save_bill(text, filename=BILL_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Bill saved to {filename}")

def main():
    print("=" * 48)
    print("          SIMPLE BILLING SYSTEM")
    print("               PROJECT PS-33")
    print("=" * 48)
    customer = input("Enter customer name: ").strip() or "Walk-in Customer"
    items = []
    while True:
        display_products()
        name = input("\nAdd item (or type 'done' to generate bill): ").strip()
        if name.lower() == "done":
            break
        qty = input("Quantity: ").strip()
        add_item(items, name, qty)

    if not items:
        print("\nNo valid items added. Bill not generated.")
        return
    bill = generate_bill(customer, items)
    print("\n" + bill)
    save_bill(bill)

if __name__ == "__main__":
    main()
