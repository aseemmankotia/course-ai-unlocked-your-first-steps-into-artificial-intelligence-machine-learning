## Chapter 4: The Brain Metaphor: Introduction to Neural Networks — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Neural Network | Computing system inspired by biological brains that processes information through connected nodes |
| Neuron | Basic unit that receives inputs, processes them, and produces an output signal |
| Layer | Group of neurons at the same level; networks have input, hidden, and output layers |
| Connections (Weights) | Links between neurons that strengthen or weaken based on learning |
| Deep Learning | Neural networks with many hidden layers, enabling complex pattern recognition |
| Training | Process of adjusting connection weights by feeding examples and correcting errors |

### Network Architecture
```
INPUT LAYER → HIDDEN LAYER(S) → OUTPUT LAYER
    ↓              ↓                ↓
 Raw data    Feature extraction   Prediction
 (pixels,    (patterns, edges,    (cat/dog,
  words)      concepts)           sentiment)
```

### Common Patterns
**Pattern 1: Forward Pass**
Data flows from input → through hidden layers → to output (making a prediction)

**Pattern 2: Learning Cycle**
Predict → Compare to correct answer → Calculate error → Adjust weights → Repeat

### Things to Remember
✅ More layers = ability to learn more abstract/complex features
✅ Networks need lots of training data to learn effectively
✅ Each layer transforms data, building on previous layer's work
❌ Neural networks aren't actual brains—they're mathematical models inspired by biology

### Quick Quiz
1. What makes deep learning "deep"? → Multiple hidden layers between input and output
2. Name 3 applications of neural networks → Image recognition, language models, generative AI