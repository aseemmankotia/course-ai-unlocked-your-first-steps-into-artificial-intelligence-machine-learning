# AI vs Machine Learning vs Deep Learning
# Let's understand the differences with a practical comparison

import random

print("🎯 Understanding AI, Machine Learning, and Deep Learning")
print("="*60)
print()

# ============================================
# APPROACH 1: Traditional AI (Rule-Based)
# ============================================
def traditional_ai_spam_detector(email):
    """
    Traditional AI: We manually define ALL the rules
    Pros: Easy to understand and explain
    Cons: Can't handle new patterns we didn't think of
    """
    spam_keywords = ['winner', 'free money', 'click here', 'prince', 'lottery']
    email_lower = email.lower()
    
    for keyword in spam_keywords:
        if keyword in email_lower:
            return "SPAM"
    return "NOT SPAM"

# ============================================
# APPROACH 2: Machine Learning (Simulated)
# ============================================
def machine_learning_spam_detector(email, learned_patterns):
    """
    Machine Learning: The system LEARNS patterns from data
    Instead of us writing rules, it discovers them!
    (This is a simplified simulation)
    """
    email_lower = email.lower()
    spam_score = 0
    
    # ML has 'learned' these patterns and their weights from data
    for pattern, weight in learned_patterns.items():
        if pattern in email_lower:
            spam_score += weight
    
    # ML learned this threshold from examples
    return "SPAM" if spam_score > 0.5 else "NOT SPAM"

# Simulated "learned" patterns (in real ML, these come from training data)
learned_patterns = {
    'urgent': 0.3,
    'act now': 0.4,
    'limited time': 0.3,
    'winner': 0.5,
    'free': 0.2,
    'click': 0.2,
    'unsubscribe': -0.3,  # Legitimate emails often have this
}

# ============================================
# APPROACH 3: Deep Learning (Conceptual)
# ============================================
def deep_learning_concept():
    """
    Deep Learning: Multiple layers of pattern recognition
    Like ML but with many layers that find increasingly complex patterns
    
    Layer 1: Recognizes individual words
    Layer 2: Recognizes phrases and context
    Layer 3: Understands intent and tone
    Layer 4+: Even more abstract patterns
    
    (Too complex to implement simply - requires libraries like TensorFlow)
    """
    return "Deep Learning uses neural networks with many layers!"

# ============================================
# Let's compare them!
# ============================================
test_emails = [
    "Congratulations! You're a WINNER! Click here for free money!",
    "Hi, can we schedule a meeting for tomorrow at 3pm?",
    "URGENT: Act now for a limited time offer!",
    "Your Amazon order has shipped. Track your package here."
]

print("📧 Comparing AI Approaches on Email Classification:")
print("-"*60)

for email in test_emails:
    print(f"\n📨 Email: \"{email[:50]}...\"" if len(email) > 50 else f"\n📨 Email: \"{email}\"")
    print(f"   🔷 Traditional AI says: {traditional_ai_spam_detector(email)}")
    print(f"   🔶 Machine Learning says: {machine_learning_spam_detector(email, learned_patterns)}")

print("\n" + "="*60)
print("🎓 KEY DIFFERENCES:")
print("-"*60)
print("""
🔷 AI (Artificial Intelligence)
   → The big umbrella term for machines that mimic human intelligence
   → Includes ALL approaches below

🔶 Machine Learning (ML)
   → A SUBSET of AI
   → Systems that LEARN from data instead of following explicit rules
   → Example: Learning spam patterns from 10,000 example emails

🔴 Deep Learning (DL)
   → A SUBSET of Machine Learning
   → Uses neural networks with MANY layers
   → Best for complex patterns (images, speech, language)
   → Example: ChatGPT, image recognition, self-driving cars

   AI  ⊃  Machine Learning  ⊃  Deep Learning
   (biggest)                    (most specialized)
""")