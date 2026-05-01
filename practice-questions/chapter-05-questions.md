## Chapter 5: AI in the Wild: Applications, Ethics & Your Next Steps — Practice Questions

### Multiple Choice

**Q1.** Which of the following is a common application of AI in healthcare?

A) Automatically writing legal contracts
B) Analyzing medical images to detect diseases
C) Composing music for relaxation therapy
D) Managing stock market investments

<details>
<summary>Answer</summary>

**Correct: B**

Analyzing medical images to detect diseases is a well-established healthcare AI application. AI systems can identify patterns in X-rays, MRIs, and CT scans to help diagnose conditions like cancer. Option A relates to legal tech, option C to creative AI, and option D to financial services—none are healthcare-specific applications.

</details>

---

**Q2.** What is "bias" in the context of AI systems?

A) A deliberate attempt by programmers to make AI systems unfair
B) Systematic errors that can lead to unfair outcomes for certain groups
C) The tendency of AI to prefer one programming language over another
D) A technical glitch that causes AI to crash unexpectedly

<details>
<summary>Answer</summary>

**Correct: B**

Bias in AI refers to systematic errors or prejudices in the system that can produce unfair outcomes, often affecting certain demographic groups more than others. This bias typically originates from training data or algorithm design, not from deliberate programmer intent (A). Options C and D describe unrelated technical concepts.

</details>

---

**Q3.** Which statement best describes a current limitation of AI systems?

A) AI cannot perform any creative tasks
B) AI systems struggle with common-sense reasoning that humans find easy
C) AI is unable to process large amounts of data
D) AI cannot recognize patterns in images

<details>
<summary>Answer</summary>

**Correct: B**

AI systems often struggle with common-sense reasoning and understanding context that humans grasp intuitively. Option A is incorrect because AI can generate creative content like art and music. Option C is wrong because processing large data is actually a strength of AI. Option D is incorrect since image recognition is one of AI's most successful applications.

</details>

---

**Q4.** What does "responsible AI" primarily focus on?

A) Making AI systems run faster and more efficiently
B) Ensuring AI systems are developed and used ethically, fairly, and transparently
C) Reducing the cost of developing AI applications
D) Limiting AI development to only large technology companies

<details>
<summary>Answer</summary>

**Correct: B**

Responsible AI focuses on ethical development and deployment, including fairness, transparency, accountability, and minimizing harm. It's about how AI impacts people and society. Options A and C focus only on technical and economic factors, while option D would actually contradict principles of accessibility and democratization in responsible AI practices.

</details>

---

**Q5.** When beginning to learn AI programming after understanding core concepts, which approach is most recommended?

A) Immediately building complex neural networks from scratch
B) Starting with practical projects using established libraries and frameworks
C) Memorizing all mathematical formulas before writing any code
D) Avoiding all tutorials and figuring everything out independently

<details>
<summary>Answer</summary>

**Correct: B**

Starting with practical projects using established libraries (like scikit-learn or TensorFlow) allows beginners to apply concepts while learning. Option A is too advanced for beginners. Option C delays hands-on learning unnecessarily, and understanding math can develop alongside coding. Option D ignores valuable learning resources that accelerate the learning process.

</details>

---

### True / False

**Q6.** AI systems can completely replace human judgment in all decision-making scenarios. — **True / False**

**False**

*AI systems have significant limitations, including lack of true understanding, inability to account for nuanced ethical considerations, and potential for bias. Many decisions—especially those involving ethics, creativity, empathy, or complex social contexts—still require human judgment. AI works best as a tool to augment human decision-making, not replace it entirely.*

---

**Q7.** Bias in AI systems can originate from the data used to train them. — **True / False**

**True**

*Training data often reflects historical human biases and societal inequalities. If an AI learns from biased data—such as hiring records that favored certain demographics—it may perpetuate or even amplify those biases. This is why careful data selection, preprocessing, and ongoing monitoring are essential parts of responsible AI development.*

---

### Short Answer

**Q8.** Name three different industries where AI is currently being applied and briefly describe one use case for each.

<details>
<summary>Answer</summary>

Example answers include:

1. **Healthcare**: AI analyzes medical images to detect tumors or diseases earlier than traditional methods.

2. **Finance**: AI systems detect fraudulent transactions by identifying unusual patterns in spending behavior.

3. **Transportation**: Self-driving vehicles use AI to perceive their environment and make navigation decisions.

4. **Retail**: AI-powered recommendation systems suggest products based on customer browsing and purchase history.

5. **Agriculture**: AI analyzes satellite imagery to monitor crop health and optimize irrigation schedules.

(Any three industries with appropriate use cases are acceptable.)

</details>

---

**Q9.** Explain why transparency is considered an important principle in responsible AI development.

<details>
<summary>Answer</summary>

Transparency in AI means making systems understandable to users and stakeholders. It's important because:

- It allows people to understand how decisions affecting them are made
- It enables identification and correction of errors or biases
- It builds trust between AI developers and the public
- It supports accountability when things go wrong
- It helps regulators and auditors verify that systems are working appropriately

When AI systems are "black boxes," it becomes difficult to challenge unfair decisions or improve system performance.

</details>

---

### Scenario-Based

**Q10.** A company develops an AI-powered hiring tool trained on their past 10 years of hiring data. After deployment, they notice the system consistently ranks male candidates higher than female candidates for technical roles. The company's historical workforce in technical positions has been 85% male.

What likely caused this bias, and what steps could the company take to address it?

<details>
<summary>Answer</summary>

**Cause of the bias:**
The AI learned from historical hiring data that reflected existing gender imbalances. Since the past workforce was predominantly male in technical roles, the system identified characteristics associated with hired candidates (who were mostly male) as indicators of "good" candidates. The AI essentially learned to replicate historical human biases present in the training data.

**Steps to address it:**

1. **Audit the training data**: Identify and understand the source of bias in historical records

2. **Balance or adjust the dataset**: Include more diverse examples or apply techniques to reduce the influence of gender-correlated features

3. **Remove or mask protected attributes**: Ensure gender (and proxies for gender) aren't directly influencing decisions

4. **Test for bias before deployment**: Evaluate the system's outcomes across different demographic groups

5. **Implement human oversight**: Have trained humans review AI recommendations, especially for final hiring decisions

6. **Continuously monitor**: Track outcomes over time to catch bias that may emerge

7. **Consider alternative approaches**: Use structured interviews or skills-based assessments that AI supports rather than controls

</details>