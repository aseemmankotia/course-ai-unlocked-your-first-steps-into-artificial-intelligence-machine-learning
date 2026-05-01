#!/bin/bash
# Verification script for Lab 3: Finding Hidden Patterns: Unsupervised Learning
set -e
echo "🔍 Verifying Lab 3: Finding Hidden Patterns: Unsupervised Learning..."
[ -f "simple-kmeans-clustering.py" ] && echo "✅ simple-kmeans-clustering.py found" || echo "❌ simple-kmeans-clustering.py missing"
[ -f "pattern-discovery-colors.py" ] && echo "✅ pattern-discovery-colors.py found" || echo "❌ pattern-discovery-colors.py missing"
echo ""
echo "✅ Lab 3 verification complete!"
