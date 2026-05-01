# A Simple AI Decision Maker
# This demonstrates the most basic form of AI: rule-based systems
# AI at its core is about making decisions based on input data

def simple_ai_advisor(temperature, is_raining):
    """
    A basic AI that gives clothing advice based on weather conditions.
    This is 'Artificial Intelligence' because it mimics human decision-making!
    """
    print("🤖 AI Weather Advisor Activated!")
    print(f"   Analyzing: Temperature = {temperature}°F, Raining = {is_raining}")
    print()
    
    # The AI's "brain" - a set of rules (this is how early AI worked!)
    if temperature < 32:
        advice = "Wear a heavy winter coat and boots!"
    elif temperature < 50:
        advice = "A warm jacket would be good."
    elif temperature < 70:
        advice = "A light sweater or long sleeves."
    else:
        advice = "T-shirt weather! Dress light."
    
    # Additional rule for rain
    if is_raining:
        advice += " Don't forget an umbrella! ☔"
    
    return advice

# Let's test our simple AI!
print("="*50)
print("Welcome to Your First AI Program!")
print("="*50)
print()

# Test different scenarios
scenarios = [
    (25, False),   # Cold and dry
    (65, True),    # Mild and rainy
    (85, False),   # Hot and sunny
]

for temp, rain in scenarios:
    result = simple_ai_advisor(temp, rain)
    print(f"💡 AI Recommendation: {result}")
    print("-"*50)
    print()

# Key Takeaway:
print("🎓 WHAT YOU LEARNED:")
print("   This is AI! It takes input, applies logic, and produces intelligent output.")
print("   Early AI systems (1950s-1980s) were mostly rule-based like this.")