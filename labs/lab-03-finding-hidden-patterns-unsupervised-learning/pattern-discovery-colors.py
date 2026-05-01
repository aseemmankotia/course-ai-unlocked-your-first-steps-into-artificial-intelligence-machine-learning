# Pattern Discovery: Finding Groups in Color Data
# The computer finds patterns - we never told it what the groups should be!

# RGB colors: [Red, Green, Blue] values from 0-255
# We're NOT telling the computer these are "warm" or "cool" colors
colors = [
    # Some reddish colors
    [255, 0, 0],      # Pure red
    [255, 100, 100],  # Light red
    [200, 50, 50],    # Dark red
    [255, 150, 150],  # Pink-ish
    
    # Some bluish colors
    [0, 0, 255],      # Pure blue
    [100, 100, 255],  # Light blue
    [50, 50, 200],    # Dark blue
    [150, 150, 255],  # Pale blue
    
    # Some greenish colors
    [0, 255, 0],      # Pure green
    [100, 255, 100],  # Light green
    [50, 200, 50],    # Forest green
]

def find_color_groups(colors, num_groups=3):
    """Group similar colors together"""
    
    # Start with some colors as group centers
    centers = [colors[0], colors[4], colors[8]]
    
    # Repeat the grouping process
    for _ in range(5):
        groups = [[], [], []]
        
        # Assign each color to nearest center
        for color in colors:
            min_distance = float('inf')
            closest = 0
            
            for i, center in enumerate(centers):
                # Color distance: how different are the RGB values?
                distance = (
                    (color[0] - center[0])**2 + 
                    (color[1] - center[1])**2 + 
                    (color[2] - center[2])**2
                )
                if distance < min_distance:
                    min_distance = distance
                    closest = i
            
            groups[closest].append(color)
        
        # Update centers to be average of their groups
        for i, group in enumerate(groups):
            if group:
                centers[i] = [
                    sum(c[0] for c in group) // len(group),
                    sum(c[1] for c in group) // len(group),
                    sum(c[2] for c in group) // len(group)
                ]
    
    return groups

# Discover the patterns!
groups = find_color_groups(colors)

print("🎨 Pattern Discovery in Colors")
print("="*40)
print("\nThe algorithm discovered these groups:\n")

for i, group in enumerate(groups):
    print(f"Group {i+1}: {len(group)} colors")
    for color in group:
        # Simple color naming based on dominant channel
        r, g, b = color
        if r > g and r > b:
            dominant = "🔴 Red-ish"
        elif g > r and g > b:
            dominant = "🟢 Green-ish"
        else:
            dominant = "🔵 Blue-ish"
        print(f"  RGB({r:3}, {g:3}, {b:3}) - {dominant}")
    print()

print("💡 Notice: We never TOLD the computer about 'red', 'green', or 'blue'!")
print("   It discovered that similar colors should be grouped together.")