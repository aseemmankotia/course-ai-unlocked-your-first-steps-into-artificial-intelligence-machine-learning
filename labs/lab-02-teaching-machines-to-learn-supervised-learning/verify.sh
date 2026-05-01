#!/bin/bash
# Verification script for Lab 2: Teaching Machines to Learn: Supervised Learning
set -e
echo "🔍 Verifying Lab 2: Teaching Machines to Learn: Supervised Learning..."
[ -f "simple-fruit-classifier.py" ] && echo "✅ simple-fruit-classifier.py found" || echo "❌ simple-fruit-classifier.py missing"
[ -f "house-price-regression.py" ] && echo "✅ house-price-regression.py found" || echo "❌ house-price-regression.py missing"
[ -f "email-spam-classifier-sklearn.py" ] && echo "✅ email-spam-classifier-sklearn.py found" || echo "❌ email-spam-classifier-sklearn.py missing"
echo ""
echo "✅ Lab 2 verification complete!"
