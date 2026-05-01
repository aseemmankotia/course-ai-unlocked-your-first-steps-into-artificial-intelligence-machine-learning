#!/bin/bash
# Verification script for Lab 4: The Brain Metaphor: Introduction to Neural Networks
set -e
echo "🔍 Verifying Lab 4: The Brain Metaphor: Introduction to Neural Networks..."
[ -f "simple-neuron-simulation.py" ] && echo "✅ simple-neuron-simulation.py found" || echo "❌ simple-neuron-simulation.py missing"
[ -f "layers-and-connections.py" ] && echo "✅ layers-and-connections.py found" || echo "❌ layers-and-connections.py missing"
echo ""
echo "✅ Lab 4 verification complete!"
