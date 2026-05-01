# House Price Predictor - Understanding REGRESSION
# Regression predicts a NUMBER (like price), not a category

# Training data: houses with their features and prices
# Features: [size_sqft, bedrooms]
# Labels: price in thousands

print("=== House Price Training Data ===")
print("Size(sqft) | Bedrooms | Price($k)")
print("-" * 35)

training_houses = [
    [1000, 2, 200],  # [size, bedrooms, price]
    [1500, 3, 300],
    [2000, 3, 400],
    [2500, 4, 500],
    [3000, 4, 600],
]

for house in training_houses:
    print(f"   {house[0]}    |    {house[1]}     |   ${house[2]}k")

# Learn the pattern: price increases by $100k per 500 sqft
# This is what the model "learns" from the data
price_per_sqft = 0.2  # $200 per sqft = $0.2k per sqft

def predict_price(size_sqft):
    """Regression model: predicts a continuous number"""
    # Simple linear relationship learned from data
    predicted_price = size_sqft * price_per_sqft
    return predicted_price

print("\n=== Model Learned ===")
print(f"Pattern found: Price ≈ Size × ${price_per_sqft}k per sqft")

# Make predictions on new houses
print("\n=== Predictions (Regression Output) ===")
test_sizes = [1200, 1800, 2200, 3500]

for size in test_sizes:
    predicted = predict_price(size)
    print(f"House with {size} sqft → Predicted price: ${predicted}k")

# Key difference from classification:
print("\n=== Classification vs Regression ===")
print("Classification: Predicts CATEGORIES (Apple or Banana)")
print("Regression: Predicts NUMBERS (Price = $350,000)")