# Email Spam Classifier - Real Supervised Learning with Scikit-Learn
# This shows how real machine learning libraries work!

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: TRAINING DATA - emails with their labels
# In real life, this would be thousands of examples!
training_emails = [
    "Win free money now click here",
    "Congratulations you won a prize",
    "Free gift card waiting for you",
    "Meeting scheduled for tomorrow",
    "Please review the attached document",
    "Lunch plans for next week?",
    "Your order has been shipped",
    "Limited time offer buy now",
]

# LABELS: 1 = spam, 0 = not spam (ham)
labels = [1, 1, 1, 0, 0, 0, 0, 1]

print("=== Training Data ===")
for email, label in zip(training_emails, labels):
    label_text = "SPAM" if label == 1 else "NOT SPAM"
    print(f"[{label_text}] {email}")

# Step 2: Convert text to numbers (machines need numbers!)
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_emails)

print(f"\n=== Learning ===")
print(f"Vocabulary learned: {len(vectorizer.get_feature_names_out())} words")
print(f"Some words: {list(vectorizer.get_feature_names_out())[:10]}...")

# Step 3: TRAIN the model - this is where learning happens!
model = MultinomialNB()
model.fit(X_train, labels)
print("Model training complete!")

# Step 4: Make PREDICTIONS on new emails
print("\n=== Testing on New Emails ===")
test_emails = [
    "Free money waiting for you",
    "Can we meet tomorrow for coffee?",
    "You won a million dollars",
    "Project deadline is next Friday",
]

X_test = vectorizer.transform(test_emails)
predictions = model.predict(X_test)

for email, prediction in zip(test_emails, predictions):
    result = "🚫 SPAM" if prediction == 1 else "✅ NOT SPAM"
    print(f"{result}: \"{email}\"")

# Show confidence scores
print("\n=== Confidence Scores ===")
probabilities = model.predict_proba(X_test)
for email, probs in zip(test_emails, probabilities):
    print(f"\"{email[:30]}...\"")
    print(f"  Not Spam: {probs[0]*100:.1f}% | Spam: {probs[1]*100:.1f}%")