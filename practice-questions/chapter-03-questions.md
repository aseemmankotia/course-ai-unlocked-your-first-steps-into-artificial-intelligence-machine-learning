## Chapter 3: Finding Hidden Patterns: Unsupervised Learning — Practice Questions

### Multiple Choice

**Q1.** What is the main difference between supervised and unsupervised learning?

A) Supervised learning is faster than unsupervised learning
B) Unsupervised learning works with labeled data while supervised learning does not
C) Supervised learning uses labeled data while unsupervised learning finds patterns without labels
D) Unsupervised learning can only work with images

<details>
<summary>Answer</summary>

**Correct: C**

Supervised learning requires labeled data where the correct answers are provided during training. Unsupervised learning discovers patterns and structures in data without any predefined labels or correct answers. Option B has it backwards, Option A is not a defining characteristic, and Option D is incorrect as unsupervised learning works with many data types.

</details>

---

**Q2.** A music streaming service wants to automatically group songs into playlists based on similar audio features, without predefined categories. Which technique would be most appropriate?

A) Supervised classification
B) Clustering
C) Linear regression
D) Manual sorting

<details>
<summary>Answer</summary>

**Correct: B**

Clustering is the unsupervised learning technique used to group similar items together based on their features. Since there are no predefined playlist categories (labels), this is an unsupervised problem. Supervised classification requires labels, linear regression predicts continuous values, and manual sorting isn't a machine learning technique.

</details>

---

**Q3.** What does "dimensionality reduction" help achieve?

A) Adding more features to your data for better accuracy
B) Simplifying data by reducing the number of features while preserving important information
C) Increasing the size of your dataset
D) Labeling data points automatically

<details>
<summary>Answer</summary>

**Correct: B**

Dimensionality reduction simplifies complex data by reducing the number of features (dimensions) while keeping the most important information intact. This makes data easier to visualize, process, and analyze. Option A describes the opposite, Option C relates to data quantity not dimensions, and Option D describes a different task entirely.

</details>

---

**Q4.** Which scenario is best suited for unsupervised learning?

A) Predicting house prices based on past sales data with known prices
B) Identifying spam emails using a dataset of emails labeled as spam or not spam
C) Discovering customer segments in shopping data without predefined customer categories
D) Teaching a computer to recognize cats using thousands of labeled cat photos

<details>
<summary>Answer</summary>

**Correct: C**

Discovering customer segments without predefined categories is ideal for unsupervised learning because you're finding natural groupings in the data. Options A, B, and D all involve labeled data (known prices, spam labels, cat labels), making them supervised learning problems.

</details>

---

**Q5.** What is a "cluster" in machine learning?

A) A type of computer processor
B) A group of similar data points grouped together by an algorithm
C) A single data point that stands out from others
D) A label assigned by a human expert

<details>
<summary>Answer</summary>

**Correct: B**

A cluster is a group of data points that an algorithm has determined to be similar to each other based on their features. Clustering algorithms automatically identify these natural groupings. Option A is unrelated to ML, Option C describes an outlier, and Option D describes labels used in supervised learning.

</details>

---

### True / False

**Q6.** Unsupervised learning always produces worse results than supervised learning because it doesn't have labels to guide it. — **True / False**

<details>
<summary>Answer</summary>

**False**

Unsupervised learning isn't inherently worse—it simply solves different problems. When you don't have labeled data or want to discover unknown patterns, unsupervised learning is the appropriate choice and can produce excellent results. Each approach has its strengths depending on the task and available data.

</details>

---

**Q7.** Clustering can help businesses discover customer segments they didn't know existed. — **True / False**

<details>
<summary>Answer</summary>

**True**

One of the key benefits of clustering is pattern discovery—finding natural groupings in data that humans might not have anticipated. A business might discover distinct customer types based on purchasing behavior, preferences, or demographics that weren't previously recognized, leading to better marketing strategies.

</details>

---

### Short Answer

**Q8.** Explain in your own words why a company might choose unsupervised learning over supervised learning when analyzing customer data.

<details>
<summary>Answer</summary>

A company might choose unsupervised learning when they don't have predefined categories for their customers or when they want to discover natural patterns they haven't thought of yet. For example, if a company wants to find customer segments but doesn't know how many groups exist or what defines them, unsupervised learning can reveal these hidden structures automatically. It's also useful when labeling large amounts of data would be too expensive or time-consuming.

</details>

---

**Q9.** Give one real-world example where dimensionality reduction would be helpful and explain why.

<details>
<summary>Answer</summary>

One example is analyzing images for a machine learning project. A single image might have thousands of pixels (features), making it computationally expensive to process. Dimensionality reduction can compress this information into fewer features while preserving the essential characteristics needed to distinguish between images. This speeds up processing, reduces storage requirements, and can even help visualize the data in 2D or 3D for human understanding.

</details>

---

### Scenario-Based

**Q10.** You work for an online bookstore. You have data on thousands of customers including their purchase history, browsing behavior, and demographics, but no predefined customer categories. Your manager asks you to find meaningful customer groups that could help personalize marketing campaigns. 

Describe the approach you would take, what type of learning this represents, and what kind of insights you might discover.

<details>
<summary>Answer</summary>

This scenario calls for **unsupervised learning**, specifically **clustering**. 

**Approach:** You would apply a clustering algorithm to the customer data, letting it group customers based on similarities in their purchasing patterns, browsing habits, and demographics.

**Why unsupervised learning:** Since there are no predefined customer categories (labels), supervised learning isn't possible. The goal is to discover natural groupings that exist in the data.

**Potential insights:** You might discover segments like "weekend readers who prefer mystery novels," "students buying textbooks seasonally," "gift buyers active around holidays," or "avid readers who purchase frequently across genres." These discovered segments could then inform targeted marketing campaigns, personalized recommendations, and tailored promotions for each group.

</details>