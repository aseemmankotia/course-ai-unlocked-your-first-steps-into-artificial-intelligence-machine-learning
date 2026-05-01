## Chapter 2: Teaching Machines to Learn: Supervised Learning — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Supervised Learning | ML approach where models learn from labeled examples with known correct answers |
| Training Data | Dataset of examples used to teach the model patterns |
| Labels | The correct answers/outputs attached to each training example |
| Classification | Predicting categories (spam/not spam, cat/dog, disease/healthy) |
| Regression | Predicting continuous numerical values (price, temperature, age) |
| Features | Input variables the model uses to make predictions |
| Model Training | Process where algorithm adjusts to minimize prediction errors |

### Key Syntax / Commands
```
Supervised Learning Formula:
INPUT (features) + LABEL (answer) → MODEL → PREDICTIONS

Classification Output: Discrete categories (A, B, C)
Regression Output: Continuous numbers (1.5, 99.7, 1000)
```

### Common Patterns
**Pattern 1: The Teacher-Student Analogy**
Teacher shows examples with answers → Student learns patterns → Student takes test on new examples

**Pattern 2: Train-Test Split**
Use ~80% data for training, ~20% for testing to evaluate model performance on unseen data

### Things to Remember
✅ More quality labeled data generally = better model performance
✅ Classification = categories; Regression = numbers (remember: "Regression = Real numbers")
✅ Labels act as the "answer key" that guides learning
✅ Real applications: email spam filters, medical diagnosis, house price prediction, credit scoring
❌ Don't confuse supervised with unsupervised (unsupervised has NO labels)
❌ Don't train and test on the same data — causes overfitting

### Quick Quiz
1. Email spam detection: classification or regression? → **Classification** (two categories)
2. Predicting house prices: classification or regression? → **Regression** (continuous values)
3. What makes learning "supervised"? → **Labeled examples with known correct answers**