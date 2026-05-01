# Simple Fruit Classifier - Understanding Supervised Learning Basics
# This example shows how a machine "learns" from labeled examples

# Step 1: Create our TRAINING DATA with LABELS
# Each fruit has features: [weight_grams, is_round (1=yes, 0=no)]
# The label tells us what fruit it is

training_data = [
    # [weight, is_round] -> label
    [150, 1],  # Apple
    [160, 1],  # Apple
    [140, 1],  # Apple
    [180, 0],  # Banana
    [190, 0],  # Banana
    [170, 0],  # Banana
]

labels = ["Apple", "Apple", "Apple", "Banana", "Banana", "Banana"]

# Step 2: Our simple "learning" - calculate averages for each fruit
# This is how the model learns patterns from examples!

apple_avg_weight = (150 + 160 + 140) / 3  # = 150
banana_avg_weight = (180 + 190 + 170) / 3  # = 183

print("=== Training Complete ===")
print(f"Learned: Apples average weight: {apple_avg_weight}g, round")
print(f"Learned: Bananas average weight: {banana_avg_weight}g, not round")

# Step 3: Make PREDICTIONS on new, unseen data
def predict_fruit(weight, is_round):
    """Our trained model makes a prediction!"""
    if is_round == 1:
        return "Apple"
    else:
        return "Banana"

# Test with new fruits the model has never seen
print("\n=== Making Predictions ===")
new_fruit_1 = [155, 1]  # Unknown fruit
new_fruit_2 = [175, 0]  # Unknown fruit

print(f"Fruit with weight={new_fruit_1[0]}g, round={new_fruit_1[1]}")
print(f"Prediction: {predict_fruit(new_fruit_1[0], new_fruit_1[1])}")

print(f"\nFruit with weight={new_fruit_2[0]}g, round={new_fruit_2[1]}")
print(f"Prediction: {predict_fruit(new_fruit_2[0], new_fruit_2[1])}")