# K-Means Clustering: Grouping Similar Things Together
# Imagine you're a store owner wanting to understand your customers

import matplotlib.pyplot as plt

# Our customer data: [amount spent per visit, visits per month]
# No labels here - we don't know what "type" of customer they are!
customers = [
    [15, 2],   # Customer 1: spends $15, visits 2x/month
    [18, 3],   # Customer 2: spends $18, visits 3x/month
    [12, 1],   # Customer 3: spends $12, visits 1x/month
    [85, 8],   # Customer 4: spends $85, visits 8x/month
    [90, 10],  # Customer 5: spends $90, visits 10x/month
    [78, 7],   # Customer 6: spends $78, visits 7x/month
    [45, 15],  # Customer 7: spends $45, visits 15x/month
    [50, 18],  # Customer 8: spends $50, visits 18x/month
    [42, 16],  # Customer 9: spends $42, visits 16x/month
]

# Simple K-Means implementation (finding 3 groups)
def simple_kmeans(data, k=3, iterations=10):
    """Find k groups in our data"""
    
    # Step 1: Start with random center points (centroids)
    centroids = data[:k]  # Just use first k points as starting centers
    
    for _ in range(iterations):
        # Step 2: Assign each point to nearest centroid
        groups = [[] for _ in range(k)]
        
        for point in data:
            # Find which centroid is closest
            distances = []
            for centroid in centroids:
                # Calculate distance (simplified: just add differences)
                dist = abs(point[0] - centroid[0]) + abs(point[1] - centroid[1])
                distances.append(dist)
            
            # Assign to closest group
            closest_group = distances.index(min(distances))
            groups[closest_group].append(point)
        
        # Step 3: Move centroids to center of their groups
        new_centroids = []
        for group in groups:
            if group:  # If group has points
                avg_x = sum(p[0] for p in group) / len(group)
                avg_y = sum(p[1] for p in group) / len(group)
                new_centroids.append([avg_x, avg_y])
            else:
                new_centroids.append(centroids[len(new_centroids)])
        centroids = new_centroids
    
    return groups, centroids

# Run clustering
groups, centers = simple_kmeans(customers, k=3)

# Display results
group_names = ["Budget Shoppers", "Premium Customers", "Frequent Visitors"]
print("🔍 Unsupervised Learning Found These Customer Groups:\n")

for i, group in enumerate(groups):
    print(f"Group {i+1} - {group_names[i]}:")
    for customer in group:
        print(f"  - Spends ${customer[0]}, visits {customer[1]}x/month")
    print()

print("✨ The algorithm found patterns WITHOUT being told what to look for!")