# Bias Detection Demo: Understanding How AI Can Learn Unfair Patterns
# This example shows how biased training data leads to biased AI decisions

import random

# Simulated historical hiring data (this reflects BIASED real-world data)
# In reality, this bias exists in many datasets and AI can amplify it

def create_biased_dataset():
    """
    Creates a dataset that reflects historical bias in hiring.
    This is intentionally biased to demonstrate the problem!
    """
    dataset = []
    
    # Historical data shows bias: certain groups were hired more often
    # This doesn't reflect ability - it reflects past discrimination
    for _ in range(100):
        candidate = {
            'years_experience': random.randint(1, 15),
            'education_level': random.choice(['bachelors', 'masters', 'phd']),
            'group': random.choice(['A', 'B'])  # Simplified demographic grouping
        }
        
        # BIASED hiring decision based on historical data
        # Group A was historically favored (this is the bias we want to detect!)
        if candidate['group'] == 'A':
            candidate['hired'] = random.random() < 0.7  # 70% hire rate
        else:
            candidate['hired'] = random.random() < 0.3  # 30% hire rate
        
        dataset.append(candidate)
    
    return dataset

def analyze_for_bias(dataset):
    """
    Analyzes the dataset to detect potential bias.
    This is a crucial step in responsible AI development!
    """
    # Count hiring rates by group
    group_stats = {'A': {'total': 0, 'hired': 0}, 'B': {'total': 0, 'hired': 0}}
    
    for candidate in dataset:
        group = candidate['group']
        group_stats[group]['total'] += 1
        if candidate['hired']:
            group_stats[group]['hired'] += 1
    
    # Calculate hiring rates
    results = {}
    for group, stats in group_stats.items():
        rate = (stats['hired'] / stats['total']) * 100 if stats['total'] > 0 else 0
        results[group] = {'rate': rate, 'total': stats['total'], 'hired': stats['hired']}
    
    return results

# Run the demonstration
print("=" * 60)
print("BIAS DETECTION IN AI TRAINING DATA")
print("=" * 60)

# Create and analyze the biased dataset
dataset = create_biased_dataset()
results = analyze_for_bias(dataset)

print("\n📊 Hiring Rate Analysis by Group:")
print("-" * 40)
for group, stats in results.items():
    print(f"Group {group}: {stats['rate']:.1f}% hired ({stats['hired']}/{stats['total']})")

# Check for significant disparity
rate_difference = abs(results['A']['rate'] - results['B']['rate'])

print("\n⚠️  BIAS ASSESSMENT:")
print("-" * 40)
if rate_difference > 20:
    print(f"❌ SIGNIFICANT BIAS DETECTED!")
    print(f"   Disparity: {rate_difference:.1f} percentage points")
    print("\n   If an AI learns from this data, it will perpetuate this bias!")
else:
    print("✓ No significant bias detected in this sample.")

print("\n💡 KEY LESSONS:")
print("-" * 40)
print("1. AI learns patterns from data - including unfair patterns")
print("2. Historical data often contains human biases")
print("3. We must audit AI systems for fairness")
print("4. Responsible AI requires diverse teams and ongoing monitoring")