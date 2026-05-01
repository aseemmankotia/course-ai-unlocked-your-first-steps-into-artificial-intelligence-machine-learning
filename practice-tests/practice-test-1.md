# AI Unlocked: Your First Steps into Artificial Intelligence &amp; Machine Learning — Practice Test 1

> **Time Limit:** 90 minutes
> **Questions:** 42
> **Passing Score:** 700/1000 (70%)
> **Generated:** 5/1/2026

---

## Instructions

- Read each question carefully
- Choose the BEST answer
- All questions are equally weighted
- Do not spend too long on any single question

---

## Questions

### Question 1
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** hard

A healthcare AI startup has developed an accurate diagnostic tool trained primarily on data from patients in developed countries. Before deploying it in a developing nation, what critical evaluation must they perform?

- A) Verify that the software runs on local computers
- B) Assess whether the model performs equally well across different populations and disease presentations that may differ in the new context
- C) Ensure the user interface is translated to local languages
- D) Confirm that the AI has a pleasant voice for audio interactions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

AI models can perform poorly on populations different from training data due to variations in genetics, disease prevalence, and presentation. Validation across target populations is essential for safety.

**Why not A:** Technical compatibility is necessary but doesn't address the critical medical accuracy concern.

**Why not C:** Language translation is important for usability but secondary to whether the AI actually works correctly for the local population.

**Why not D:** Voice quality is a minor UX concern compared to the life-or-death accuracy of medical diagnoses.

**Exam Tip:** AI trained on one population may not generalize to others—validation on target populations is essential, especially in healthcare.

</details>

---

### Question 2
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** easy

What is algorithmic bias in AI systems?

- A) When an algorithm runs too slowly on certain computers
- B) When AI systems produce unfair outcomes that systematically favor or disadvantage certain groups
- C) When programmers intentionally make the AI produce wrong answers
- D) When an AI system uses too much electricity

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Algorithmic bias occurs when AI systems produce systematically unfair results, often reflecting historical biases in training data or flawed assumptions in model design.

**Why not A:** Performance speed differences relate to computational efficiency, not fairness or bias concerns.

**Why not C:** Intentional errors would be sabotage or malicious coding, which is different from systematic bias that often occurs unintentionally.

**Why not D:** Energy consumption is an environmental concern, not related to the fairness or bias of AI decisions.

**Exam Tip:** AI bias often comes from biased training data—if historical data contains discrimination, the AI learns it.

</details>

---

### Question 3
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** medium

A data scientist notices that her neural network performs extremely well on training data (99% accuracy) but poorly on new test data (65% accuracy). What problem is most likely occurring?

- A) Underfitting due to insufficient model complexity
- B) Overfitting where the model memorized training data instead of learning general patterns
- C) The learning rate is set too low
- D) The activation functions are not working properly

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Overfitting occurs when a model learns the training data too well, including noise and outliers, resulting in excellent training performance but poor generalization to new data.

**Why not A:** Underfitting would show poor performance on BOTH training and test data, not just test data.

**Why not C:** A low learning rate would slow training but wouldn't cause this specific pattern of high training/low test accuracy.

**Why not D:** Activation function issues would affect both training and test performance similarly, not create this disparity.

**Exam Tip:** Large gap between training and test accuracy = overfitting; poor performance on both = underfitting.

</details>

---

### Question 4
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** hard

Which statement accurately describes why AI experienced 'winters' (periods of reduced funding and interest) historically?

- A) AI researchers intentionally slowed progress to prevent dangerous superintelligent systems
- B) Government regulations banned AI research during these periods
- C) Overpromising capabilities followed by underdelivering led to disillusionment among funders and the public
- D) Hardware technology was advancing too quickly for AI algorithms to keep pace

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

AI winters occurred when early AI systems failed to meet ambitious predictions. Researchers promised human-level translation, reasoning, and understanding, but the technology couldn't deliver, causing funders to withdraw support.

**Why not A:** AI winters were not intentional. They resulted from unmet expectations, not deliberate slowdowns for safety concerns.

**Why not B:** No government bans caused AI winters. The slowdowns were driven by economic and scientific disappointment, not regulatory action.

**Why not D:** The relationship was opposite - hardware limitations were one factor constraining AI capabilities, not that hardware was too advanced.

**Exam Tip:** AI winters teach us to be realistic about AI capabilities - hype cycles followed by disappointment

</details>

---

### Question 5
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** medium

A social media company's AI content recommendation system is found to be promoting increasingly extreme content to users because engagement metrics reward emotional reactions. What ethical concern does this represent?

- A) Data privacy violation
- B) Unintended consequences and potential societal harm from optimizing for narrow metrics
- C) Lack of model accuracy
- D) Insufficient training data

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Optimizing AI for engagement without considering broader impacts can lead to unintended harmful consequences, such as promoting divisive content that damages social discourse.

**Why not A:** While related to data use, the core issue is the harmful optimization objective, not privacy.

**Why not C:** The model is accurately optimizing for its goal (engagement); the problem is that the goal itself causes harm.

**Why not D:** Insufficient data would reduce performance; this system is performing as designed—the design itself is problematic.

**Exam Tip:** AI systems do exactly what they're optimized for—ensuring objectives align with human values is critical.

</details>

---

### Question 6
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** easy

What is the defining characteristic of supervised learning that distinguishes it from other machine learning approaches?

- A) It requires human supervision during every prediction the model makes
- B) It learns from labeled data where inputs are paired with known correct outputs
- C) It can only be used for image recognition tasks
- D) It doesn't require any data to make predictions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Supervised learning uses training data with labeled examples - each input has a corresponding correct output (label). The algorithm learns the mapping between inputs and outputs to predict labels for new, unseen data.

**Why not A:** Human supervision is only needed during training to provide labels. Once trained, the model makes predictions independently without human involvement.

**Why not C:** Supervised learning applies to many tasks beyond images: predicting prices, classifying emails, forecasting demand, medical diagnosis, and countless other applications.

**Why not D:** Supervised learning requires substantial labeled data for training. The quality and quantity of training data significantly impact model performance.

**Exam Tip:** The 'supervision' in supervised learning refers to labeled training data, not ongoing human oversight

</details>

---

### Question 7
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** medium

A real estate company builds a model to predict the exact sale price of houses based on features like square footage, location, and number of bedrooms. The model performs excellently on training data but poorly on new listings. What problem is MOST likely occurring?

- A) Underfitting - the model is too simple to capture patterns
- B) Overfitting - the model memorized training data instead of learning generalizable patterns
- C) The model needs more training epochs to converge
- D) The features selected are completely irrelevant to house prices

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Overfitting occurs when a model learns the training data too well, including noise and outliers, failing to generalize to new data. High training accuracy with poor test performance is the classic overfitting signature.

**Why not A:** Underfitting shows poor performance on both training AND test data. Here, training performance is excellent, indicating the model captured patterns (perhaps too many).

**Why not C:** More training would likely worsen overfitting by further memorizing training data. The model already performs well on training data; more training won't help generalization.

**Why not D:** Square footage, location, and bedrooms are highly relevant to house prices. If features were irrelevant, the model wouldn't perform well even on training data.

**Exam Tip:** Good training performance + poor test performance = overfitting

</details>

---

### Question 8
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** hard

A medical diagnostic model is trained to detect a rare disease that affects 1% of patients. The model predicts 'no disease' for every patient and achieves 99% accuracy. Why is this model problematic despite the high accuracy?

- A) The model is overfitting to the training data
- B) 99% accuracy is insufficient for medical applications
- C) The model fails to identify any actual disease cases, making it useless for its intended purpose despite high accuracy on imbalanced data
- D) The training data must contain labeling errors

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

With 99% healthy patients, predicting everyone as healthy yields 99% accuracy while detecting zero disease cases. This is the class imbalance problem - accuracy is misleading when classes are unequal. Metrics like recall, precision, or F1-score are needed.

**Why not A:** This isn't overfitting (memorizing training data). The model is actually underfitting by not learning the disease pattern at all - it's just predicting the majority class.

**Why not B:** The issue isn't the accuracy threshold. A legitimate 99% accurate medical model could be valuable. The problem is HOW this accuracy is achieved - by ignoring the minority class entirely.

**Why not D:** Labeling errors aren't indicated here. The problem is the learning algorithm's response to imbalanced classes, not data quality.

**Exam Tip:** Accuracy is misleading for imbalanced datasets - always check precision, recall, and confusion matrix

</details>

---

### Question 9
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** easy

What is the fundamental building block of a neural network that receives inputs, applies weights, and produces an output?

- A) A hidden layer
- B) An artificial neuron (perceptron)
- C) A training dataset
- D) A loss function

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

An artificial neuron or perceptron is the basic computational unit that receives weighted inputs, sums them, applies an activation function, and produces an output—mimicking biological neurons.

**Why not A:** A hidden layer is a collection of neurons between input and output layers, not the fundamental building block itself.

**Why not C:** A training dataset is the data used to teach the network, not a structural component of the neural network architecture.

**Why not D:** A loss function measures prediction errors during training but is not a building block of the network structure.

**Exam Tip:** Remember: neurons are to neural networks what cells are to organisms—the basic unit of structure and function.

</details>

---

### Question 10
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** medium

A bank wants to build a model that predicts whether loan applicants will default (yes/no) based on their credit history, income, and employment status. What type of supervised learning task is this?

- A) Regression, because it involves financial data
- B) Classification, because the output is a discrete category (default or not)
- C) Clustering, because it groups similar applicants together
- D) Dimensionality reduction, because it reduces the number of input features

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Classification predicts discrete categories or classes. Since the output is binary (yes/no, default/no default), this is a classification problem. The model assigns each applicant to one of two classes.

**Why not A:** Regression predicts continuous numerical values (like exact dollar amounts). The output here is a category (default vs. no default), not a continuous number.

**Why not C:** Clustering is unsupervised learning that groups similar items without predefined labels. This task has specific labels (default/no default), making it supervised classification.

**Why not D:** Dimensionality reduction reduces features, not makes predictions. It's a preprocessing technique, not a prediction task type.

**Exam Tip:** Classification = categories/classes; Regression = continuous numbers

</details>

---

### Question 11
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** easy

What does it mean when we say traditional programming differs from Machine Learning?

- A) Traditional programming is faster than Machine Learning
- B) Traditional programming requires explicit rules; Machine Learning derives rules from data
- C) Machine Learning can only work with numerical data
- D) Traditional programming cannot be combined with Machine Learning

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

In traditional programming, developers explicitly write rules (if-then logic). In Machine Learning, algorithms discover patterns and rules from data. You provide examples, and the system learns the underlying rules.

**Why not A:** Speed depends on the task. Some ML operations are faster; some traditional code is faster. This isn't the fundamental distinction.

**Why not C:** Machine Learning can process text, images, audio, and other data types, not just numbers. Data is often converted to numerical representations, but inputs can be diverse.

**Why not D:** Traditional programming and ML are frequently combined. Most AI applications use conventional programming for data handling, user interfaces, and integration, with ML for pattern recognition.

**Exam Tip:** Traditional = programmer writes rules; ML = system learns rules from examples

</details>

---

### Question 12
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** hard

A deep learning team is training a 50-layer neural network but observes that gradients become extremely small in early layers, causing those layers to learn very slowly. What technique specifically addresses this problem?

- A) Using dropout regularization
- B) Implementing skip connections (residual connections)
- C) Increasing the batch size
- D) Adding more neurons to each layer

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Skip connections allow gradients to flow directly through shortcut paths, bypassing layers and preventing the vanishing gradient problem that plagues very deep networks.

**Why not A:** Dropout helps prevent overfitting by randomly disabling neurons but doesn't address vanishing gradients.

**Why not C:** Larger batch sizes affect training stability and generalization but don't solve the gradient flow problem in deep networks.

**Why not D:** More neurons increase capacity but don't help gradients propagate through many layers.

**Exam Tip:** Vanishing gradients in deep networks are solved by skip/residual connections (ResNets) or specialized activation functions.

</details>

---

### Question 13
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** hard

A financial services company uses an AI model to approve loans. Regulators require them to explain why specific applicants were denied. The company uses a complex deep learning model that provides high accuracy but cannot easily explain individual decisions. What approach should they implement?

- A) Remove the AI system entirely and return to manual processing
- B) Use explainable AI (XAI) techniques like LIME or SHAP to provide post-hoc explanations
- C) Simply tell applicants they were denied due to 'AI analysis'
- D) Only approve loans and never deny anyone to avoid explanation requirements

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Explainable AI techniques like LIME and SHAP can analyze complex models and generate human-understandable explanations for individual predictions, meeting regulatory requirements while keeping the model.

**Why not A:** Completely removing AI sacrifices accuracy benefits; XAI techniques can preserve both performance and explainability.

**Why not C:** Vague explanations don't satisfy regulatory requirements for specific, actionable reasons for denial.

**Why not D:** Approving everyone defeats the purpose of risk assessment and would expose the company to massive financial risk.

**Exam Tip:** XAI bridges the gap between model accuracy and regulatory requirements for explanation in high-stakes decisions.

</details>

---

### Question 14
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** hard

During backpropagation, what mathematical technique is used to calculate how much each weight contributed to the overall error?

- A) Matrix multiplication
- B) The chain rule of calculus
- C) Random sampling
- D) Fourier transformation

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The chain rule allows backpropagation to compute gradients layer by layer, determining how changes in each weight affect the final error by chaining partial derivatives together.

**Why not A:** Matrix multiplication is used in forward propagation to compute outputs, but gradient calculation specifically relies on the chain rule.

**Why not C:** Random sampling might be used in mini-batch selection but is not the technique for calculating weight contributions to error.

**Why not D:** Fourier transformation converts signals between time and frequency domains and is not used in standard backpropagation.

**Exam Tip:** Backpropagation = chain rule applied backwards through the network to find gradients for each weight.

</details>

---

### Question 15
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** medium

A machine learning engineer notices that training loss decreases very slowly and takes hundreds of epochs to converge. Which hyperparameter adjustment is most likely to speed up training?

- A) Decrease the number of hidden layers
- B) Increase the learning rate
- C) Add more training examples
- D) Change from ReLU to Sigmoid activation

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

A higher learning rate takes larger steps during gradient descent, potentially speeding up convergence when the current rate is too conservative.

**Why not A:** Reducing hidden layers would simplify the model but wouldn't directly address slow convergence due to small update steps.

**Why not C:** More training examples would increase computation per epoch and likely slow down training further.

**Why not D:** Switching to Sigmoid could actually worsen the problem due to vanishing gradient issues in deep networks.

**Exam Tip:** Slow convergence often indicates learning rate is too low; oscillating loss suggests it's too high.

</details>

---

### Question 16
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** medium

An engineer is building a neural network to classify images into 10 different categories (cat, dog, bird, etc.). Which activation function should be used in the OUTPUT layer?

- A) ReLU (Rectified Linear Unit)
- B) Sigmoid
- C) Softmax
- D) Tanh (Hyperbolic Tangent)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Softmax is ideal for multi-class classification as it converts raw outputs into probability distributions across all classes, where probabilities sum to 1.

**Why not A:** ReLU is commonly used in hidden layers but doesn't produce probability distributions needed for multi-class classification.

**Why not B:** Sigmoid is suitable for binary classification (yes/no) but not for selecting among multiple categories.

**Why not D:** Tanh outputs values between -1 and 1, which doesn't represent class probabilities appropriately for multi-class problems.

**Exam Tip:** Output layer activation depends on the task: Softmax for multi-class, Sigmoid for binary, Linear for regression.

</details>

---

### Question 17
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** easy

What distinguishes a 'Narrow AI' system from 'Artificial General Intelligence' (AGI)?

- A) Narrow AI requires more computational power than AGI
- B) Narrow AI excels at specific tasks while AGI would match human-level intelligence across all cognitive domains
- C) Narrow AI is theoretical while AGI systems are currently deployed worldwide
- D) Narrow AI uses neural networks while AGI uses traditional programming

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Narrow AI (also called Weak AI) is designed for specific tasks like chess, image recognition, or language translation. AGI would theoretically possess human-like reasoning and learning capabilities across any intellectual task.

**Why not A:** Computational requirements don't define the difference. In fact, AGI (if achieved) would likely require far more resources than current narrow AI systems.

**Why not C:** This is reversed. Narrow AI exists today (Siri, recommendation systems, etc.), while AGI remains theoretical and has not been achieved.

**Why not D:** The distinction isn't about the underlying technology. Both could potentially use neural networks or other approaches; the difference is in scope of capability.

**Exam Tip:** All current AI systems are Narrow AI - AGI remains a future goal that hasn't been achieved

</details>

---

### Question 18
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** easy

What is the PRIMARY function of an algorithm in the context of AI and Machine Learning?

- A) To store large amounts of training data in databases
- B) To provide a step-by-step procedure for solving problems or making decisions
- C) To connect AI systems to the internet for real-time updates
- D) To create user interfaces for interacting with AI systems

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

An algorithm is a defined sequence of instructions or rules that processes input data to produce an output. In ML, algorithms are the mathematical procedures that learn patterns from data to make predictions or decisions.

**Why not A:** Data storage is handled by databases and storage systems, not algorithms. Algorithms process data but don't store it.

**Why not C:** Network connectivity is an infrastructure concern, not the function of an algorithm. Algorithms can work offline with available data.

**Why not D:** User interfaces are designed separately by UI/UX developers. Algorithms handle the computational logic, not the visual presentation.

**Exam Tip:** Think of algorithms as recipes - they define the exact steps to transform inputs into outputs

</details>

---

### Question 19
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** medium

A retail company wants to use AI to personalize customer experiences. The privacy officer is concerned about data collection practices. Which principle should guide their AI implementation?

- A) Collect as much data as possible to improve AI accuracy
- B) Data minimization—collect only the data necessary for the specific purpose
- C) Store all data indefinitely in case it becomes useful later
- D) Share data freely with third parties to enhance AI capabilities

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Data minimization is a key privacy principle requiring organizations to collect only data necessary for the stated purpose, reducing privacy risks while still enabling AI benefits.

**Why not A:** Excessive data collection violates privacy principles and increases breach risks without proportional benefit.

**Why not C:** Indefinite retention conflicts with data protection regulations that require retention limits and purpose specification.

**Why not D:** Unrestricted sharing violates consent and privacy laws; data sharing requires legal basis and user consent.

**Exam Tip:** Privacy-respecting AI follows: collect only what you need, use it only as stated, delete it when done.

</details>

---

### Question 20
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** easy

In a feedforward neural network, in what direction does information flow during prediction?

- A) From output layer to input layer
- B) Randomly between all layers
- C) From input layer through hidden layers to output layer
- D) In a circular loop through all layers repeatedly

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

In feedforward networks, information flows in one direction—forward from input through hidden layers to output—without any cycles or loops.

**Why not A:** Information flowing backward describes backpropagation during training, not the prediction/inference phase.

**Why not B:** Random flow would make the network unpredictable and unable to produce consistent outputs.

**Why not D:** Circular loops describe recurrent neural networks (RNNs), not standard feedforward networks.

**Exam Tip:** Feedforward = one-way street from input to output. Recurrent networks have loops for sequential data.

</details>

---

### Question 21
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** medium

A small business owner wants to use AI to predict which products will sell best next month. They have sales records from the past 3 years. What type of AI approach would be MOST appropriate for this task?

- A) Robotics Process Automation to physically count inventory
- B) Machine Learning to identify patterns in historical sales data
- C) Natural Language Processing to read product descriptions
- D) Computer Vision to analyze product packaging designs

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Machine Learning excels at finding patterns in historical data to make predictions. With 3 years of sales records, ML algorithms can identify seasonal trends, correlations, and patterns to forecast future product demand.

**Why not A:** Robotics Process Automation handles repetitive rule-based tasks, not predictive analytics. Physical counting doesn't predict future sales.

**Why not C:** While NLP could analyze product reviews, the core task of sales prediction from numerical sales data is a statistical ML problem, not a language processing task.

**Why not D:** Computer Vision analyzes images. While package design might influence sales, the direct prediction from sales history requires numerical pattern recognition, not image analysis.

**Exam Tip:** Prediction from historical data = Machine Learning (supervised learning specifically)

</details>

---

### Question 22
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** medium

An e-commerce company wants to predict the exact dollar amount each customer will spend next month. The data science team has historical purchase data with customer demographics and past spending. Which algorithm type is MOST appropriate?

- A) Logistic Regression for binary classification
- B) K-Means for customer segmentation
- C) Linear Regression or Random Forest Regression for continuous value prediction
- D) Principal Component Analysis for feature extraction

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Predicting exact dollar amounts is a regression problem requiring algorithms that output continuous values. Linear Regression provides interpretability while Random Forest Regression handles complex non-linear relationships.

**Why not A:** Logistic Regression, despite its name, is for classification (predicting categories like 'high spender' vs 'low spender'), not continuous dollar amounts.

**Why not B:** K-Means is unsupervised clustering, not prediction. It groups similar customers but doesn't predict specific spending amounts.

**Why not D:** PCA reduces dimensions for preprocessing. It doesn't make predictions; it transforms features for other algorithms to use.

**Exam Tip:** Predicting continuous numbers = regression algorithms

</details>

---

### Question 23
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** hard

A startup is building a neural network to predict house prices (a continuous value). During testing, they notice the model always predicts values close to the average price regardless of input features. What is the most likely cause?

- A) The output layer uses Softmax activation instead of linear activation
- B) The learning rate is too high, causing the model to overshoot optimal weights
- C) The training data contains too many unique house prices
- D) The model has too many hidden layers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: A**

This is the correct answer.

**Why not B:** A high learning rate would cause erratic predictions, not consistently average ones.

**Why not C:** Diverse prices in training data would help the model learn variation, not cause average-only predictions.

**Why not D:** Too many layers might cause other issues, but wouldn't specifically cause predictions to collapse to the mean.

**Exam Tip:** Match activation to task type: Linear for regression, Sigmoid for binary classification, Softmax for multi-class.

</details>

---

### Question 24
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** medium

Which supervised learning algorithm creates decision boundaries by finding the optimal line or hyperplane that maximizes the margin between different classes?

- A) Linear Regression
- B) Support Vector Machine (SVM)
- C) K-Nearest Neighbors (KNN)
- D) Naive Bayes

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Support Vector Machines find the hyperplane that maximizes the margin (distance) between classes. The support vectors are the data points closest to this boundary that define it.

**Why not A:** Linear Regression predicts continuous values, not classifications. It fits a line to minimize error, not maximize margins between classes.

**Why not C:** KNN classifies based on the majority class among K nearest neighbors. It doesn't create explicit decision boundaries or optimize margins.

**Why not D:** Naive Bayes uses probability calculations based on Bayes' theorem and feature independence assumptions. It doesn't optimize geometric margins.

**Exam Tip:** SVM = maximum margin classifier; finds the widest possible gap between classes

</details>

---

### Question 25
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** medium

A hiring company implements an AI resume screening tool. After six months, data shows that qualified female candidates are being filtered out at higher rates than equally qualified male candidates. What is the most likely cause?

- A) The AI was programmed to discriminate intentionally
- B) The training data reflected historical hiring patterns that favored male candidates
- C) Female candidates submitted lower quality resumes
- D) The AI randomly makes mistakes on female candidates

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

If historical hiring data showed bias toward male candidates, the AI learned to replicate this pattern. The model optimizes to match past decisions, perpetuating existing biases.

**Why not A:** Intentional discrimination is rare; most AI bias stems from biased data or proxy variables, not explicit programming.

**Why not C:** This explanation assumes the bias is justified, which contradicts the premise that candidates were equally qualified.

**Why not D:** Systematic bias affecting one group consistently indicates a pattern, not random errors.

**Exam Tip:** Historical bias in training data leads to AI that perpetuates discrimination—garbage in, garbage out.

</details>

---

### Question 26
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** easy

Which industry has widely adopted AI for detecting fraudulent transactions in real-time?

- A) Agriculture
- B) Financial services and banking
- C) Construction
- D) Mining

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Financial services extensively use AI to analyze transaction patterns and detect fraud in real-time, protecting consumers and institutions from financial crimes.

**Why not A:** Agriculture uses AI for crop monitoring and yield prediction, but fraud detection isn't a primary application.

**Why not C:** Construction uses AI for project management and safety, not primarily for fraud detection.

**Why not D:** Mining uses AI for exploration and safety, but fraud detection isn't a major application area.

**Exam Tip:** Financial fraud detection is a classic AI success story—analyzing millions of transactions instantly to spot anomalies.

</details>

---

### Question 27
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** medium

A hospital administrator is evaluating AI solutions and hears claims about a system that can 'diagnose any disease, perform surgery, write research papers, and counsel patients emotionally with human-level expertise.' What should the administrator conclude?

- A) This represents cutting-edge AGI technology now available in healthcare
- B) These claims describe capabilities beyond current AI, which remains limited to narrow, specific tasks
- C) This is standard Machine Learning applied across multiple hospital departments
- D) This describes Deep Learning systems that have achieved general intelligence

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Current AI is Narrow AI, designed for specific tasks. A system claiming expertise across diagnosis, surgery, writing, and emotional counseling describes AGI capabilities that don't exist. Each task would require separate, specialized AI systems.

**Why not A:** AGI (Artificial General Intelligence) has not been achieved. No current system possesses human-level intelligence across multiple unrelated domains.

**Why not C:** Standard Machine Learning creates specialized models for specific tasks. A model trained for diagnosis cannot perform surgery or provide counseling without separate training.

**Why not D:** Deep Learning, despite being powerful, still produces narrow AI systems. No Deep Learning system has achieved general intelligence across diverse tasks.

**Exam Tip:** Be skeptical of AI claims that suggest general-purpose intelligence - current AI is always task-specific

</details>

---

### Question 28
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** medium

What does the term 'epoch' refer to in neural network training?

- A) The time it takes to train one neuron
- B) One complete pass through the entire training dataset
- C) The final accuracy achieved by the model
- D) The number of layers in the network

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

An epoch represents one complete iteration through all training examples, after which the model has seen every sample once for weight updates.

**Why not A:** Training time per neuron is not a standard metric; epochs measure passes through data, not computational time.

**Why not C:** Final accuracy is a performance metric, not a training iteration term.

**Why not D:** The number of layers describes network depth, which is an architectural decision unrelated to training iterations.

**Exam Tip:** Training terminology: Epoch = full dataset pass; Batch = subset processed together; Iteration = one batch update.

</details>

---

### Question 29
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** easy

What are 'features' in the context of supervised machine learning?

- A) The predictions made by the model
- B) The input variables used to make predictions
- C) The errors in the model's predictions
- D) The hardware specifications required to run the model

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Features are the input variables (also called attributes or predictors) that the model uses to make predictions. In a house price model, features might include square footage, number of rooms, and location.

**Why not A:** Model predictions are called outputs, predictions, or in classification, predicted labels. Features are inputs, not outputs.

**Why not C:** Prediction errors are called residuals or loss, not features. Features exist before any prediction is made.

**Why not D:** Hardware specifications are infrastructure requirements, unrelated to the data-science concept of features in machine learning.

**Exam Tip:** Features = inputs (X variables); Labels/Targets = outputs (Y variable)

</details>

---

### Question 30
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** hard

Which factor has been MOST critical in enabling recent AI breakthroughs compared to earlier AI research periods?

- A) Development of fundamentally new algorithms that didn't exist before 2010
- B) The combination of massive datasets, increased computing power, and improved algorithms working together
- C) Achievement of Artificial General Intelligence allowing machines to learn anything
- D) Replacement of all traditional programming with AI-only software development

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Modern AI success comes from three converging factors: big data provides training material, powerful GPUs/TPUs enable complex computations, and refined algorithms (some dating back decades) can now be implemented effectively. No single factor alone caused the breakthrough.

**Why not A:** Many core algorithms (like backpropagation, 1986) existed for decades. Recent advances improved and combined existing approaches rather than inventing entirely new ones.

**Why not C:** AGI has not been achieved. Current breakthroughs are in Narrow AI - impressive but limited to specific domains.

**Why not D:** Traditional programming remains essential. AI complements conventional software; it hasn't replaced it. Most applications combine AI with traditional code.

**Exam Tip:** Remember the three pillars of modern AI: Data + Compute + Algorithms

</details>

---

### Question 31
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** medium

What does the term 'AI accountability' primarily refer to?

- A) Keeping track of how much AI costs to operate
- B) Ensuring there are clear responsibilities for AI decisions and mechanisms to address harms
- C) Counting the number of AI systems a company uses
- D) Recording how many predictions an AI makes per day

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

AI accountability ensures that humans or organizations are responsible for AI system outcomes, with clear processes to address errors, biases, or harms caused by AI decisions.

**Why not A:** Cost tracking is financial management, not ethical accountability for AI decisions and their impacts.

**Why not C:** Counting systems is inventory management, unrelated to the ethical responsibility for AI actions.

**Why not D:** Prediction logging is operational monitoring, not accountability for the consequences of those predictions.

**Exam Tip:** Accountability answers: 'Who is responsible when AI makes a harmful decision?' There must always be a human answer.

</details>

---

### Question 32
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** easy

Which of the following is a common application of AI in healthcare?

- A) Automatically generating hospital buildings
- B) Analyzing medical images to assist in disease detection
- C) Physically performing surgery without any human involvement
- D) Replacing all doctors with AI systems

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

AI excels at analyzing medical images like X-rays, MRIs, and pathology slides, helping radiologists detect diseases like cancer earlier and more accurately.

**Why not A:** Building generation is not a current AI healthcare application; construction uses different technologies.

**Why not C:** While surgical robots exist, they are human-controlled; fully autonomous surgery without human involvement is not a current practice.

**Why not D:** AI augments and assists doctors rather than replacing them; healthcare requires human judgment and patient interaction.

**Exam Tip:** AI in healthcare = augmentation, not replacement. It helps doctors make better decisions faster.

</details>

---

### Question 33
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** hard

A data scientist builds a model to predict customer churn. The model has 95% precision but only 40% recall. What does this performance indicate about the model's behavior?

- A) The model correctly identifies most churning customers but with many false positives
- B) When the model predicts churn, it's usually correct, but it misses the majority of actual churning customers
- C) The model is performing equally well on both churning and non-churning customers
- D) The model needs more training data to improve both metrics

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

High precision (95%) means predictions of churn are usually correct. Low recall (40%) means the model only catches 40% of actual churners. It's conservative - rarely wrong when it predicts churn, but misses 60% of churning customers.

**Why not A:** This describes high recall with low precision (catching most churners but with false alarms). Our model has the opposite pattern - high precision, low recall.

**Why not C:** The metrics show imbalanced performance. High precision with low recall indicates the model is much better at avoiding false positives than catching true positives.

**Why not D:** While more data might help, this doesn't describe what the current metrics indicate about model behavior.

**Exam Tip:** Precision = 'When I predict positive, am I right?' Recall = 'Did I catch all actual positives?'

</details>

---

### Question 34
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** medium

A hospital implements an AI system to prioritize patients for a new treatment program. Analysis reveals that the system consistently ranks patients from wealthy neighborhoods higher than equally sick patients from lower-income areas. What ethical principle is being violated?

- A) Transparency
- B) Fairness and equity
- C) Data minimization
- D) Model interpretability

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Fairness and equity require that AI systems treat individuals equitably regardless of socioeconomic status. Systematically disadvantaging lower-income patients violates this principle.

**Why not A:** Transparency concerns whether the system's workings are understandable, not whether its outcomes are equitable.

**Why not C:** Data minimization relates to collecting only necessary data, not to fair treatment in outcomes.

**Why not D:** Interpretability concerns understanding how decisions are made, which is related but distinct from whether outcomes are fair.

**Exam Tip:** Fairness means similar individuals should receive similar treatment regardless of protected characteristics.

</details>

---

### Question 35
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** medium

A retail company wants to implement a system that can automatically sort customer emails into categories like 'Returns,' 'Product Questions,' and 'Complaints' without human intervention. Which type of AI capability is MOST directly required?

- A) Computer Vision for reading email attachments
- B) Natural Language Processing for understanding text content
- C) Robotics for automated physical sorting
- D) Speech Recognition for converting voice messages

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Natural Language Processing (NLP) enables machines to understand, interpret, and categorize human language in text form. Email classification requires understanding the meaning and intent behind written customer messages.

**Why not A:** Computer Vision processes images and videos, not text. While it might help with image attachments, the core task of understanding email content requires NLP.

**Why not C:** Robotics involves physical automation. Email sorting is a digital classification task that doesn't require any physical manipulation.

**Why not D:** Speech Recognition converts spoken words to text. Since emails are already in text format, this capability isn't needed for this task.

**Exam Tip:** Match AI capabilities to the data type: text = NLP, images = Computer Vision, speech = Speech Recognition

</details>

---

### Question 36
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** easy

Which of the following best describes the relationship between Artificial Intelligence, Machine Learning, and Deep Learning?

- A) They are three completely separate and unrelated fields of study
- B) Machine Learning is a subset of AI, and Deep Learning is a subset of Machine Learning
- C) AI is a subset of Machine Learning, which is a subset of Deep Learning
- D) Deep Learning and Machine Learning are the same thing, both subsets of AI

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

AI is the broadest field encompassing any machine that mimics human intelligence. Machine Learning is a specific approach within AI where systems learn from data. Deep Learning is a specialized subset of ML using neural networks with multiple layers.

**Why not A:** These fields are hierarchically related, not separate. Each builds upon and is contained within the broader field above it.

**Why not C:** This reverses the actual relationship. AI is the largest umbrella term, not the smallest subset.

**Why not D:** Deep Learning and Machine Learning are distinct. Deep Learning specifically uses multi-layered neural networks, while ML includes many other algorithms like decision trees and linear regression.

**Exam Tip:** Remember the nested relationship: AI > ML > DL (like Russian nesting dolls)

</details>

---

### Question 37
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** medium

What is the purpose of the bias term in a neural network neuron?

- A) To store previous predictions for comparison
- B) To allow the neuron to shift its activation function and output non-zero values even when all inputs are zero
- C) To prevent the network from learning incorrect patterns
- D) To reduce the computational cost of training

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The bias acts as an offset, allowing the neuron to shift its activation threshold and produce meaningful outputs even with zero inputs, increasing the network's flexibility.

**Why not A:** Storing previous predictions describes memory mechanisms in recurrent networks, not the function of bias terms.

**Why not C:** Preventing incorrect learning is the role of regularization and proper training, not bias terms.

**Why not D:** Bias terms add a small computational cost; they're included for model flexibility, not efficiency.

**Exam Tip:** Bias = flexibility. Like the y-intercept in y=mx+b, it shifts the function without changing its shape.

</details>

---

### Question 38
**Domain:** Teaching Machines to Learn: Supervised Learning | **Difficulty:** easy

In supervised learning, what is the purpose of splitting data into training and test sets?

- A) To make the training process faster by using less data
- B) To evaluate how well the model performs on data it hasn't seen during training
- C) To ensure the model only learns from the best quality examples
- D) To create backup copies of the data in case of data loss

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The test set acts as unseen data that evaluates whether the model learned generalizable patterns or just memorized training examples. Performance on test data estimates real-world performance on new data.

**Why not A:** Speed isn't the reason for splitting. In fact, using less training data might reduce model quality. The purpose is evaluation, not efficiency.

**Why not C:** Both training and test sets should represent the full data quality range. Selecting only 'best' examples would create unrealistic evaluation conditions.

**Why not D:** This isn't about backup or data safety. Train-test split is a model evaluation methodology, not a data storage practice.

**Exam Tip:** Test data = measuring real-world performance before deployment

</details>

---

### Question 39
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** hard

A technology executive claims their new AI system 'thinks and reasons exactly like a human brain.' Based on current scientific understanding, which response is MOST accurate?

- A) This is accurate because neural networks perfectly replicate biological neuron function
- B) This is an overstatement; AI systems use mathematical approximations inspired by brains but process information fundamentally differently
- C) This is accurate because Deep Learning has achieved consciousness
- D) This cannot be verified because we fully understand how human brains work

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

While neural networks are loosely inspired by brains, they're mathematical models, not biological replicas. They use different mechanisms (matrix multiplication vs. electrochemical signals) and lack consciousness, common sense, and general reasoning abilities of human minds.

**Why not A:** Artificial neurons are simplified mathematical functions that don't replicate the complexity of biological neurons, which involve neurotransmitters, synaptic plasticity, and thousands of connections.

**Why not C:** No AI system has achieved consciousness. Deep Learning produces sophisticated pattern recognition, but consciousness and understanding remain exclusively biological phenomena.

**Why not D:** This reasoning is flawed. We don't fully understand human brains, but we do understand enough to know that current AI operates differently - using algorithms, not biological processes.

**Exam Tip:** Be cautious about claims that AI 'thinks' like humans - it's a useful metaphor but not literally accurate

</details>

---

### Question 40
**Domain:** The Brain Metaphor: Introduction to Neural Networks | **Difficulty:** easy

What is the primary purpose of an activation function in a neural network?

- A) To store the training data for later use
- B) To introduce non-linearity so the network can learn complex patterns
- C) To reduce the number of neurons needed in each layer
- D) To speed up the training process by skipping unnecessary calculations

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Activation functions introduce non-linearity, allowing neural networks to learn and represent complex, non-linear relationships in data that simple linear combinations cannot capture.

**Why not A:** Activation functions don't store data; they transform the output of neurons mathematically.

**Why not C:** Activation functions don't affect the number of neurons; network architecture decisions determine neuron count.

**Why not D:** Activation functions actually add computational steps; they don't skip calculations but transform outputs.

**Exam Tip:** Without activation functions, a neural network would just be a series of linear transformations—unable to learn complex patterns.

</details>

---

### Question 41
**Domain:** What's All the Fuss About? Demystifying AI | **Difficulty:** medium

A startup founder reads that 'AI will automate all jobs within 5 years' in a news article, while an academic paper states 'AI will augment human workers in specific tasks.' Which interpretation reflects a more accurate understanding of current AI capabilities?

- A) The news article, because AI progress is exponential and will soon achieve AGI
- B) Both are equally accurate representations of mainstream AI research consensus
- C) The academic paper, because current AI excels at specific tasks rather than replacing entire jobs
- D) Neither, because AI has stopped advancing and cannot impact employment

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Current AI is Narrow AI that automates specific tasks, not entire jobs. Most jobs contain tasks AI cannot perform. The academic view of AI augmenting workers aligns with current capabilities and research consensus.

**Why not A:** While AI is progressing, AGI remains theoretical. Exponential progress in narrow tasks doesn't translate to human-level general intelligence or total job replacement.

**Why not B:** These views are not equally accurate. Mainstream research supports task augmentation, while total automation claims are typically sensationalized media coverage.

**Why not D:** AI continues advancing rapidly. The question isn't whether AI impacts employment, but how - through augmentation rather than complete replacement.

**Exam Tip:** Distinguish between AI automating tasks versus replacing entire jobs - usually it's task augmentation

</details>

---

### Question 42
**Domain:** AI in the Wild: Applications, Ethics & Your Next Steps | **Difficulty:** hard

What is 'AI safety' primarily concerned with as a field of study?

- A) Protecting AI systems from computer viruses
- B) Ensuring AI systems behave as intended and don't cause unintended harm as they become more capable
- C) Making sure AI code is written without syntax errors
- D) Keeping AI hardware in secure physical locations

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

AI safety focuses on ensuring AI systems remain beneficial and aligned with human values, especially as systems become more powerful and autonomous, preventing catastrophic unintended consequences.

**Why not A:** Cybersecurity for AI is important but is a subset of general security, not the specific field of AI safety research.

**Why not C:** Code correctness is software engineering quality, not the broader concern of whether AI systems are safe for society.

**Why not D:** Physical security is facility management, separate from the research field addressing AI alignment and safety.

**Exam Tip:** AI safety asks: How do we ensure powerful AI systems do what we actually want, not just what we literally programmed?

</details>

---

## Answer Key

| Q | Answer | Domain | Difficulty |
|---|--------|--------|-----------|
| 1 | B | AI in the Wild: Applications, Ethics & Your Next Steps | hard |
| 2 | B | AI in the Wild: Applications, Ethics & Your Next Steps | easy |
| 3 | B | The Brain Metaphor: Introduction to Neural Networks | medium |
| 4 | C | What's All the Fuss About? Demystifying AI | hard |
| 5 | B | AI in the Wild: Applications, Ethics & Your Next Steps | medium |
| 6 | B | Teaching Machines to Learn: Supervised Learning | easy |
| 7 | B | Teaching Machines to Learn: Supervised Learning | medium |
| 8 | C | Teaching Machines to Learn: Supervised Learning | hard |
| 9 | B | The Brain Metaphor: Introduction to Neural Networks | easy |
| 10 | B | Teaching Machines to Learn: Supervised Learning | medium |
| 11 | B | What's All the Fuss About? Demystifying AI | easy |
| 12 | B | The Brain Metaphor: Introduction to Neural Networks | hard |
| 13 | B | AI in the Wild: Applications, Ethics & Your Next Steps | hard |
| 14 | B | The Brain Metaphor: Introduction to Neural Networks | hard |
| 15 | B | The Brain Metaphor: Introduction to Neural Networks | medium |
| 16 | C | The Brain Metaphor: Introduction to Neural Networks | medium |
| 17 | B | What's All the Fuss About? Demystifying AI | easy |
| 18 | B | What's All the Fuss About? Demystifying AI | easy |
| 19 | B | AI in the Wild: Applications, Ethics & Your Next Steps | medium |
| 20 | C | The Brain Metaphor: Introduction to Neural Networks | easy |
| 21 | B | What's All the Fuss About? Demystifying AI | medium |
| 22 | C | Teaching Machines to Learn: Supervised Learning | medium |
| 23 | A | The Brain Metaphor: Introduction to Neural Networks | hard |
| 24 | B | Teaching Machines to Learn: Supervised Learning | medium |
| 25 | B | AI in the Wild: Applications, Ethics & Your Next Steps | medium |
| 26 | B | AI in the Wild: Applications, Ethics & Your Next Steps | easy |
| 27 | B | What's All the Fuss About? Demystifying AI | medium |
| 28 | B | The Brain Metaphor: Introduction to Neural Networks | medium |
| 29 | B | Teaching Machines to Learn: Supervised Learning | easy |
| 30 | B | What's All the Fuss About? Demystifying AI | hard |
| 31 | B | AI in the Wild: Applications, Ethics & Your Next Steps | medium |
| 32 | B | AI in the Wild: Applications, Ethics & Your Next Steps | easy |
| 33 | B | Teaching Machines to Learn: Supervised Learning | hard |
| 34 | B | AI in the Wild: Applications, Ethics & Your Next Steps | medium |
| 35 | B | What's All the Fuss About? Demystifying AI | medium |
| 36 | B | What's All the Fuss About? Demystifying AI | easy |
| 37 | B | The Brain Metaphor: Introduction to Neural Networks | medium |
| 38 | B | Teaching Machines to Learn: Supervised Learning | easy |
| 39 | B | What's All the Fuss About? Demystifying AI | hard |
| 40 | B | The Brain Metaphor: Introduction to Neural Networks | easy |
| 41 | C | What's All the Fuss About? Demystifying AI | medium |
| 42 | B | AI in the Wild: Applications, Ethics & Your Next Steps | hard |

---

## Domain Score Tracker

| Domain | Questions | Your Score |
|--------|-----------|------------|
| What's All the Fuss About? Demystifying AI | 11 | /11 |
| Teaching Machines to Learn: Supervised Learning | 11 | /11 |
| Finding Hidden Patterns: Unsupervised Learning | 11 | /11 |
| The Brain Metaphor: Introduction to Neural Networks | 11 | /11 |
| AI in the Wild: Applications, Ethics & Your Next Steps | 11 | /11 |

*Fill in as you check your answers*
