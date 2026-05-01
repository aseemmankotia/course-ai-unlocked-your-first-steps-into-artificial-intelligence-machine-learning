#!/bin/bash
# Verification script for Lab 5: AI in the Wild: Applications, Ethics & Your Next Steps
set -e
echo "🔍 Verifying Lab 5: AI in the Wild: Applications, Ethics & Your Next Steps..."
[ -f "sentiment-analyzer-demo.py" ] && echo "✅ sentiment-analyzer-demo.py found" || echo "❌ sentiment-analyzer-demo.py missing"
[ -f "bias-detection-demo.py" ] && echo "✅ bias-detection-demo.py found" || echo "❌ bias-detection-demo.py missing"
echo ""
echo "✅ Lab 5 verification complete!"
