print("Welcome to ticket sales\n")

MAX_TICKETS = 16

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    if quantity < 1:
        print("sorry, must order at least one ticket")
        continue
    if quantity > 16:
        print("sorry, the maximum is 16")
        continue

    print(f"sending {quantity} ticket(s)")

