## Chapter 4: The Brain Metaphor: Introduction to Neural Networks — Practice Questions

### Multiple Choice

**Q1.** What is the basic processing unit in a neural network, inspired by biological brain cells?

A) Layer
B) Neuron
C) Algorithm
D) Database

<details>
<summary>Answer</summary>

**Correct: B**

A neuron is the basic processing unit in a neural network, inspired by how biological neurons work in the brain. Layers are collections of neurons, algorithms are the overall procedures, and databases are storage systems unrelated to neural network structure.

</details>

---

**Q2.** What makes deep learning "deep" compared to traditional neural networks?

A) It uses more powerful computers
B) It processes data more slowly but accurately
C) It has many layers stacked together
D) It only works with images

<details>
<summary>Answer</summary>

**Correct: C**

Deep learning is called "deep" because it uses neural networks with many layers (often dozens or hundreds) stacked together. The depth refers to the number of layers, not computing power, speed, or data type limitations.

</details>

---

**Q3.** How do the connections between neurons in a neural network primarily store learned information?

A) In a separate database file
B) Through weights assigned to connections
C) By memorizing all training examples
D) In the computer's RAM temporarily

<details>
<summary>Answer</summary>

**Correct: B**

Neural networks store learned information through weights assigned to the connections between neurons. During training, these weights are adjusted to improve the network's performance. The knowledge isn't stored separately or memorized as exact copies of training data.

</details>

---

**Q4.** Which of the following is NOT a common application of neural networks?

A) Recognizing faces in photographs
B) Generating human-like text responses
C) Performing simple arithmetic calculations
D) Creating AI-generated artwork

<details>
<summary>Answer</summary>

**Correct: C**

Simple arithmetic calculations don't require neural networks—basic programming can handle them easily. Neural networks excel at complex pattern recognition tasks like image recognition, language processing, and generative AI, which are difficult to program with traditional rules.

</details>

---

**Q5.** In a typical neural network architecture, what is the role of the hidden layers?

A) To display the final output to users
B) To receive the initial input data
C) To process and transform data between input and output
D) To store backup copies of the data

<details>
<summary>Answer</summary>

**Correct: C**

Hidden layers sit between the input and output layers and are responsible for processing and transforming data. They extract increasingly complex features and patterns from the data. The input layer receives data, the output layer produces results, and neural networks don't store backups.

</details>

---

### True / False

**Q6.** Neural networks can learn to perform tasks without being explicitly programmed with step-by-step rules for every situation. — **True / False**

<details>
<summary>Answer</summary>

**True**

This is one of the key advantages of neural networks. Instead of requiring programmers to write explicit rules for every scenario, neural networks learn patterns from examples during training. For instance, an image recognition network learns what cats look like by seeing many cat photos, rather than being programmed with rules like "cats have pointy ears."

</details>

---

**Q7.** A neural network with only one layer can be considered a deep learning model. — **True / False**

<details>
<summary>Answer</summary>

**False**

Deep learning specifically refers to neural networks with multiple layers (typically many layers). A single-layer network is called a shallow network or simple perceptron. The "deep" in deep learning indicates the depth created by stacking many layers together, which allows the network to learn more complex patterns.

</details>

---

### Short Answer

**Q8.** Explain in your own words how a neural network "learns" from data at a conceptual level.

<details>
<summary>Answer</summary>

A neural network learns by adjusting the weights of connections between neurons based on how well it performs. During training, the network makes predictions, compares them to the correct answers, and then adjusts its connection weights to reduce errors. This process repeats many times with many examples until the network becomes accurate. It's similar to learning through practice and feedback—getting better by correcting mistakes over time.

</details>

---

**Q9.** Name and briefly describe the three main types of layers found in a typical neural network.

<details>
<summary>Answer</summary>

The three main types of layers are:

1. **Input Layer**: Receives the initial data (such as pixel values from an image or words from text) and passes it into the network.

2. **Hidden Layers**: Process and transform the data through weighted connections. These layers extract patterns and features, with each successive layer often learning more complex representations.

3. **Output Layer**: Produces the final result or prediction, such as a classification label, a probability, or generated content.

</details>

---

### Scenario-Based

**Q10.** A hospital wants to develop a system that can analyze X-ray images and highlight areas that might show signs of pneumonia. They have collected 50,000 labeled X-ray images (some showing pneumonia, some healthy). Explain why a deep neural network would be suitable for this task and describe the general process of how the system would be developed.

<details>
<summary>Answer</summary>

A deep neural network is well-suited for this medical imaging task for several reasons:

**Why it's suitable:**
- Image recognition is a strength of deep learning, especially with convolutional neural networks
- The task requires identifying complex visual patterns that are difficult to define with explicit rules
- 50,000 labeled images provide enough training data for the network to learn

**Development process:**
1. **Data preparation**: Organize the X-rays into training, validation, and test sets with their labels (pneumonia or healthy)
2. **Network design**: Choose an appropriate deep neural network architecture with multiple layers capable of learning visual features
3. **Training**: Feed images through the network, letting it adjust its weights based on whether it correctly identifies pneumonia cases
4. **Validation**: Test the network on images it hasn't seen to ensure it generalizes well
5. **Refinement**: Adjust the network based on performance, potentially adding more layers or training data
6. **Deployment**: Once accurate enough, integrate the system into the hospital's workflow as a diagnostic aid for radiologists

</details>