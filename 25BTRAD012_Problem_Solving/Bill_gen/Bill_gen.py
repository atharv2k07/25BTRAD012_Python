# Simple Restaurant Bill Generator

menu = {
    1: ("Margherita Pizza", 250),
    2: ("Veg Burger", 120),
    3: ("White Sauce Pasta", 180),
    4: ("French Fries", 90),
    5: ("Cold Coffee", 100)
}

order = []

print("--- WELCOME TO PYTHON CAFE ---")
print("Menu:")
for code, (item, price) in menu.items():
    print(f"{code}. {item} - Rs. {price}")

while True:
    choice = int(input("\nEnter item number (0 to finish): "))
    if choice == 0:
        break
    elif choice in menu:
        qty = int(input(f"Enter quantity for {menu[choice][0]}: "))
        order.append((menu[choice][0], menu[choice][1], qty))
    else:
        print("Invalid item number!")

# Calculate and print bill
subtotal = 0
print("\n" + "=" * 38)
print("           RESTAURANT BILL")
print("=" * 38)
print(f"{'Item':<20}{'Qty':<6}{'Amount':>10}")
print("-" * 38)

for item, price, qty in order:
    amount = price * qty
    subtotal += amount
    print(f"{item:<20}{qty:<6}{amount:>10.2f}")

gst = subtotal * 0.05
grand_total = subtotal + gst

print("-" * 38)
print(f"{'Subtotal:':<26}{subtotal:>10.2f}")
print(f"{'GST (5%):':<26}{gst:>10.2f}")
print("=" * 38)
print(f"{'Grand Total:':<26}{grand_total:>10.2f}")
print("=" * 38)
print("     Thank you! Visit again!")