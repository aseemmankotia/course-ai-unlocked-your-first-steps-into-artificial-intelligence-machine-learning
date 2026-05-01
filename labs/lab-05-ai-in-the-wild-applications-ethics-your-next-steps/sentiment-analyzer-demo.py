# Sentiment Analysis Demo: How AI Helps Businesses Understand Customer Feedback
# This demonstrates a simplified version of what companies use to analyze reviews

# In real applications, this would use machine learning models
# Here we use a rule-based approach to understand the concept

def analyze_sentiment(text):
    """
    A simple sentiment analyzer that checks for positive and negative words.
    Real AI systems use much more sophisticated approaches!
    """
    # Lists of words that indicate sentiment
    positive_words = ['good', 'great', 'excellent', 'amazing', 'love', 'best', 
                      'fantastic', 'wonderful', 'happy', 'satisfied', 'helpful']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'poor', 
                      'disappointed', 'frustrated', 'angry', 'useless', 'broken']
    
    # Convert to lowercase for comparison
    text_lower = text.lower()
    
    # Count positive and negative words
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    # Determine overall sentiment
    if positive_count > negative_count:
        return "POSITIVE", positive_count, negative_count
    elif negative_count > positive_count:
        return "NEGATIVE", positive_count, negative_count
    else:
        return "NEUTRAL", positive_count, negative_count

# Example customer reviews
reviews = [
    "This product is amazing! Best purchase I've ever made.",
    "Terrible experience. The product arrived broken and customer service was useless.",
    "It's okay, nothing special but gets the job done.",
    "I love how helpful the staff was. Great service!",
    "Disappointed with the quality. Expected better for the price."
]

# Analyze each review
print("=" * 60)
print("CUSTOMER REVIEW SENTIMENT ANALYSIS")
print("=" * 60)

for i, review in enumerate(reviews, 1):
    sentiment, pos, neg = analyze_sentiment(review)
    print(f"\nReview {i}: \"{review[:50]}...\"" if len(review) > 50 else f"\nReview {i}: \"{review}\"")
    print(f"  Sentiment: {sentiment}")
    print(f"  Positive indicators: {pos} | Negative indicators: {neg}")

# Show limitations
print("\n" + "=" * 60)
print("LIMITATIONS OF THIS SIMPLE APPROACH:")
print("=" * 60)
print("- Cannot understand sarcasm ('Great, another broken product')")
print("- Misses context and nuance")
print("- Limited vocabulary")
print("- Real AI uses neural networks trained on millions of examples!")