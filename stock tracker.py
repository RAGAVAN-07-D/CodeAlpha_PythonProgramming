# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 130,
    "MSFT": 320
}

# Store user portfolio
portfolio = {}

print("Enter your stock portfolio. Type 'done' when finished.")

# Take user input
while True:
    stock = input("Stock symbol: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio Summary:")
print("------------------------")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print("------------------------")
print(f"Total Investment Value: ${total_value}")

# Optionally save to file
save = input("\nSave to file? (yes/no): ").lower()
if save == 'yes':
    file_format = input("Choose file format - txt or csv: ").lower()
    if file_format == 'txt':
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("------------------------\n")
            for stock, quantity in portfolio.items():
                f.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock]*quantity}\n")
            f.write(f"Total Investment Value: ${total_value}\n")
        print("Saved as portfolio.txt")
    elif file_format == 'csv':
        import csv
        with open("portfolio.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                writer.writerow([stock, quantity, price, price*quantity])
            writer.writerow(["Total", "", "", total_value])
        print("Saved as portfolio.csv")
    else:
        print("Invalid format. Not saved.")
