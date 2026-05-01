#!/bin/bash
# Verification script for Lab 1: What's All the Fuss About? Demystifying AI
set -e
echo "🔍 Verifying Lab 1: What's All the Fuss About? Demystifying AI..."
[ -f "simple-ai-decision-maker.py" ] && echo "✅ simple-ai-decision-maker.py found" || echo "❌ simple-ai-decision-maker.py missing"
[ -f "ai-ml-dl-comparison.py" ] && echo "✅ ai-ml-dl-comparison.py found" || echo "❌ ai-ml-dl-comparison.py missing"
echo ""
echo "✅ Lab 1 verification complete!"
