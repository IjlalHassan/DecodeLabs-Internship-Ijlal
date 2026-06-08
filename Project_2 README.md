# Data Classification Using KNN (Iris Dataset)

A machine learning project that classifies iris flowers into 3 species using the K-Nearest Neighbors algorithm.

## What It Does

- Loads the Iris dataset (150 samples, 4 features)
- Splits data 80/20 for training and testing
- Scales features using StandardScaler
- Trains a KNN classifier (k=5)
- Outputs accuracy, confusion matrix, and F1 score

## Results

| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| F1 Score (macro avg) | 1.00 |

Confusion Matrix:
```
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

## Tech Stack

- Python 3.11
- scikit-learn
- pandas
- Jupyter Notebook

## How to Run

1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies
```bash
pip install scikit-learn pandas jupyter
```

3. Launch the notebook
```bash
jupyter notebook Project_2.ipynb
```

4. Run all cells (Kernel > Restart & Run All)

## Dataset

Iris dataset from `sklearn.datasets` — no external CSV needed. Loads automatically.

## Classes Predicted

- Setosa
- Versicolor
- Virginica

## Author

Ijlal — BS Artificial Intelligence, Karachi, Pakistan
