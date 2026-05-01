# A single neuron: the basic building block of neural networks
# Think of it like a tiny decision maker in your brain!

def simple_neuron(inputs, weights, bias):
    """
    A neuron takes inputs, multiplies them by weights,
    adds a bias, and decides whether to 'fire' or not.
    
    inputs: list of numbers (like signals from other neurons)
    weights: how important each input is
    bias: the neuron's personal preference
    """
    # Step 1: Multiply each input by its weight and sum them up
    weighted_sum = 0
    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]
        print(f"  Input {i+1}: {inputs[i]} × Weight {weights[i]} = {inputs[i] * weights[i]}")
    
    # Step 2: Add the bias
    total = weighted_sum + bias
    print(f"  Weighted sum: {weighted_sum} + Bias {bias} = {total}")
    
    # Step 3: Activation function (decides if neuron 'fires')
    # Using a simple threshold: if total > 0, output 1; otherwise 0
    if total > 0:
        output = 1  # Neuron fires!
    else:
        output = 0  # Neuron stays quiet
    
    return output

# Example: Should I go outside?
# Inputs: [is it sunny?, do I have free time?]
print("=" * 50)
print("NEURON EXAMPLE: Should I go outside?")
print("=" * 50)

inputs = [1, 1]  # 1 = yes, 0 = no (sunny AND free time)
weights = [0.6, 0.4]  # Sunny weather matters more to me
bias = -0.5  # I'm a bit of a homebody

print("\nInputs: [Sunny=1, Free time=1]")
print("Processing...")
result = simple_neuron(inputs, weights, bias)
print(f"\nDecision: {'GO OUTSIDE! 🌞' if result == 1 else 'Stay inside 🏠'}")

# Try different scenarios
print("\n" + "=" * 50)
print("What if it's cloudy but I have free time?")
print("=" * 50)
inputs = [0, 1]  # Not sunny, but have free time
print("\nInputs: [Sunny=0, Free time=1]")
print("Processing...")
result = simple_neuron(inputs, weights, bias)
print(f"\nDecision: {'GO OUTSIDE! 🌞' if result == 1 else 'Stay inside 🏠'}")