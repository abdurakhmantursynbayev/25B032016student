prices = [499.99, 1200.00, 350.50, 2500.00, 899.99, 1050.00]

for i, price in enumerate(prices, start=1):
    print(f"  {i}. {price:.2f}")

expensive = list(filter(lambda p: p > 1000, prices))
print(f"Expensive items: {expensive}")
print(f"Total: {sum(expensive):.2f}")
# Expensive items: [1200.0, 2500.0, 1050.0]
# Total: 4750.00