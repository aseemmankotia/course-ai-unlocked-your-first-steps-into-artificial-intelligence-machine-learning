## Chapter 2: Teaching Machines to Learn: Supervised Learning — Practice Questions

### Multiple Choice

**Q1.** What makes supervised learning "supervised"?

A) A human watches the computer while it learns
B) The model learns from data that includes correct answers (labels)
C) The computer supervises other computers during training
D) The learning process requires constant internet connection

<details>
<summary>Answer</summary>

**Correct: B**

Supervised learning gets its name because the training data includes labels—the correct answers that guide the model's learning, similar to a student learning with an answer key. Option A is incorrect because humans don't need to watch the process. Option C describes something that doesn't exist. Option D is unrelated to the concept of supervision in machine learning.

</details>

---

**Q2.** Which of the following is an example of a classification problem?

A) Predicting tomorrow's temperature in degrees
B) Estimating the price of a house
C) Determining whether an email is spam or not spam
D) Forecasting next month's sales revenue

<details>
<summary>Answer</summary>

**Correct: C**

Classification involves sorting data into distinct categories or groups. Determining spam vs. not spam involves placing emails into one of two categories. Options A, B, and D are all regression problems because they predict continuous numerical values (temperature, price, and revenue) rather than categories.

</details>

---

**Q3.** In supervised learning, what is "training data"?

A) Data the model has never seen before
B) A collection of examples with known inputs and correct outputs
C) Random numbers used to test the model
D) The final predictions made by the model

<details>
<summary>Answer</summary>

**Correct: B**

Training data consists of examples that include both the input information and the corresponding correct answers (labels). This data is used to teach the model patterns. Option A describes test data. Option C is incorrect as training data is not random. Option D describes model outputs, not inputs.

</details>

---

**Q4.** A bank wants to predict the exact dollar amount a customer might spend next month. What type of supervised learning problem is this?

A) Classification
B) Regression
C) Clustering
D) Labeling

<details>
<summary>Answer</summary>

**Correct: B**

Regression is used when predicting continuous numerical values, like a specific dollar amount. Classification would be used for categories (like "high spender" vs. "low spender"). Clustering is an unsupervised learning technique. Labeling is part of data preparation, not a type of learning problem.

</details>

---

**Q5.** What role do labels play in supervised learning?

A) They make the dataset larger
B) They tell the model what the correct answer should be for each example
C) They speed up the computer's processing power
D) They are optional and only used for advanced models

<details>
<summary>Answer</summary>

**Correct: B**

Labels are the correct answers attached to training examples. They teach the model what output to associate with each input, enabling it to learn patterns. Labels don't affect dataset size (A) or processing speed (C), and they are essential—not optional—for supervised learning (D).

</details>

---

### True / False

**Q6.** A model that predicts whether a tumor is "benign" or "malignant" is performing regression. — **True / False**

*False. This is a classification problem because the model is sorting tumors into distinct categories (benign or malignant) rather than predicting a continuous number. Regression would involve predicting a numerical value, such as the size of a tumor in millimeters.*

---

**Q7.** Supervised learning requires humans to provide labeled examples before the model can learn. — **True / False**

*True. Supervised learning depends on labeled data—examples where the correct answer is already known. Humans typically create these labels (like tagging photos as "cat" or "dog") so the model can learn the relationship between inputs and outputs.*

---

### Short Answer

**Q8.** Explain the difference between classification and regression in your own words, and give one example of each.

<details>
<summary>Answer</summary>

Classification predicts which category something belongs to, choosing from a set of distinct options. Example: Identifying whether a photo contains a cat or a dog.

Regression predicts a continuous numerical value that can fall anywhere on a scale. Example: Predicting the selling price of a house based on its features.

</details>

---

**Q9.** Why is high-quality labeled data important for training a supervised learning model?

<details>
<summary>Answer</summary>

High-quality labeled data is essential because the model learns patterns directly from these examples. If labels are incorrect, inconsistent, or biased, the model will learn wrong patterns and make poor predictions. The principle "garbage in, garbage out" applies—a model can only be as good as the data it learns from.

</details>

---

### Scenario-Based

**Q10.** A streaming service wants to build an AI system that recommends movies to users. They have collected data showing which movies each user has watched and rated on a 1-5 star scale. 

**Part A:** Is this a supervised learning problem? Why or why not?

**Part B:** If they wanted to predict a user's exact star rating for a new movie, would this be classification or regression?

**Part C:** If instead they wanted to predict whether a user would "like" or "dislike" a movie, how would your answer to Part B change?

<details>
<summary>Answer</summary>

**Part A:** Yes, this is a supervised learning problem. The user ratings serve as labels—they provide the correct answer (how much the user liked each movie) paired with input features (the movie and user information).

**Part B:** This would be regression because star ratings are numerical values on a continuous scale (1-5), and the model is predicting a specific number.

**Part C:** This would become classification because "like" and "dislike" are two distinct categories. The model would be sorting predictions into groups rather than predicting a number.

</details>

---