# Neural networks have LAYERS of neurons connected together
# Input Layer → Hidden Layer(s) → Output Layer
# This is like passing a message through a chain of friends!

import math

def sigmoid(x):
    """Activation function that squishes values between 0 and 1"""
    return 1 / (1 + math.exp(-x))

def create_layer(num_neurons, num_inputs):
    """Create a layer with random-ish weights"""
    import random
    random.seed(42)  # For reproducibility
    layer = []
    for _ in range(num_neurons):
        neuron = {
            'weights': [random.uniform(-1, 1) for _ in range(num_inputs)],
            'bias': random.uniform(-1, 1)
        }
        layer.append(neuron)
    return layer

def forward_pass(inputs, layer):
    """Pass inputs through a layer of neurons"""
    outputs = []
    for neuron in layer:
        # Calculate weighted sum + bias
        total = neuron['bias']
        for i, inp in enumerate(inputs):
            total += inp * neuron['weights'][i]
        # Apply activation function
        output = sigmoid(total)
        outputs.append(output)
    return outputs

# Build a simple 3-layer network
print("🧠 BUILDING A SIMPLE NEURAL NETWORK")
print("=" * 50)
print("\nNetwork Structure:")
print("  Input Layer:  2 inputs (your data)")
print("  Hidden Layer: 3 neurons (the 'thinking' layer)")
print("  Output Layer: 1 neuron (the answer)")
print("\nThis is what makes deep learning 'deep' - multiple layers!")

# Create our layers
hidden_layer = create_layer(num_neurons=3, num_inputs=2)
output_layer = create_layer(num_neurons=1, num_inputs=3)

# Example: Classify a point (is it in the top-right quadrant?)
print("\n" + "=" * 50)
print("RUNNING THE NETWORK")
print("=" * 50)

# Test with different inputs
test_inputs = [
    [0.8, 0.9],   # Top-right area
    [-0.5, -0.5], # Bottom-left area
    [0.3, 0.7],   # Somewhere in between
]

for inputs in test_inputs:
    print(f"\n📥 Input: {inputs}")
    
    # Forward pass through hidden layer
    hidden_output = forward_pass(inputs, hidden_layer)
    print(f"   Hidden layer output: {[f'{x:.3f}' for x in hidden_output]}")
    
    # Forward pass through output layer
    final_output = forward_pass(hidden_output, output_layer)
    print(f"   📤 Final output: {final_output[0]:.3f}")
    print(f"   Interpretation: {'Likely top-right ✓' if final_output[0] > 0.5 else 'Likely not top-right ✗'}")

print("\n" + "=" * 50)
print("KEY INSIGHT: Each layer transforms the data,")
print("finding patterns that help make the final decision!")
print("=" * 50)