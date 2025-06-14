

## 🎯 Final Model Selection for AI Career Counsellor

### ✅ Objective:

Build a system that takes user interests/skills/hobbies as input and predicts:

* 🎓 The most suitable **Course** (single best option)
* 💼 A list of recommended **Career Options** (multiple possible outcomes)

---

## 📊 Task Breakdown

| Task                         | Type of Problem                | Description                                               |
| ---------------------------- | ------------------------------ | --------------------------------------------------------- |
| 🎓 Courses Prediction        | **Multi-Class Classification** | Predict one correct course from multiple possible classes |
| 💼 Career Options Prediction | **Multi-Label Classification** | Predict multiple relevant careers for a user              |

---

## ✅ Final Model Choices

### 1. 🎓 Courses → **Random Forest Classifier**

* **Why Random Forest?**

  * Achieved **higher F1 score and accuracy** than Neural Networks in our experiments.
  * **Fast to train**, easy to interpret and deploy.
  * Works well with **structured, categorical, binary input** like our 0/1 feature vector.
* **Result**:

  * Accuracy: `99.43%`
  * F1 Score: `0.94`

**Saved File:**
`random_forest_courses_model.pkl`

---

### 2. 💼 Career Options → **Neural Network (Keras Sequential Model)**

* **Why Neural Network?**

  * Outperformed Random Forest in **macro F1-score for multi-label classification**.
  * Neural networks are better suited for **multi-output binary classification tasks**.
  * Flexible to adapt in the future with embedding-based features (if needed).
* **Result**:

  * Hamming Loss: `0.000305`
  * Macro F1 Score: `0.8140`

**Saved File:**
`career_model.h5`

---

## 🧩 Supporting Components (Needed for Prediction)

These files are essential for processing new user input during runtime:

| Component                   | Purpose                                            | File Name                   |
| --------------------------- | -------------------------------------------------- | --------------------------- |
| `LabelEncoder` for Courses  | Converts predicted class index back to course name | `courses_label_encoder.pkl` |
| `MultiLabelBinarizer`       | Decodes NN outputs into career option names        | `career_options_mlb.pkl`    |

---

## ❌ Files You Do NOT Need

| File                                     | Reason                                            |
| ---------------------------------------- | ------------------------------------------------- |
| `random_forest_career_options_model.pkl` | You are using Neural Network for this task        |
| `courses_model.h5`                       | You are using Random Forest for course prediction |

---

## ✅ Final Model Files to Use

```
- random_forest_courses_model.pkl
- career_model.h5
- courses_label_encoder.pkl
- career_options_mlb.pkl
```

These models can be loaded and used inside a **Streamlit frontend** or a **Rasa-powered NLP chatbot**.

---


