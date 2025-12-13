# Hierarchical Clustering Analysis

## Coded By: 
Miguel Angel Pafalox Gomez [GitHub](https://github.com/ter-kes) [clustering]
Bhavik Bhagat [GitHub](https://github.com/bhavik-knight) [Executed SQL in Python]
Md Chistia Chowdhury [Provided SQL Query]

## 1. Overview

This project contains a Python script designed to perform **hierarchical agglomerative clustering** on supplier data based on the products they supply.

The analysis uses the **Jaccard Distance** metric to quantify dissimilarity between suppliers based on their product portfolios and visualizes these relationships using a **dendrogram**.

---

## 2. Dependencies

The script requires the following Python packages:

- **pandas** — data loading and manipulation  
- **scipy** — distance calculation and hierarchical clustering  
  - `pdist`
  - `linkage`
- **matplotlib** — visualization (dendrogram plotting)  
- **openpyxl** — required by pandas to read `.xlsx` files  

---

## 3. Setup and Installation

This project uses **`uv`** for fast and isolated dependency management.

### A. Install `uv`

If `uv` is not already installed, install it using your terminal.

Reference: [uv documentation](https://docs.astral.sh/uv/getting-started/installation/)

Windows (after running the command restart terminal):
```bash
winget install astral-sh.uv
```

Linux/Mac:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 4. Clone the project from Github
```bash
git clone 
```

### 5. Install dependencies
```bash
uv sync
```

### 6. Execute the script
```bash
uv run clustering.py
```

## 7. Output

The script generates two main outputs:

### Console Output
Prints messages during execution (if any are added).

### Visualization Output
A saved image file (e.g., `dendrogram.png`) displaying the **Hierarchical Agglomerative Clustering dendrogram**.  
This plot illustrates the relationships between suppliers based on their product similarity.

---

## 7. Core Logic Details

### Data Preparation
- Performs **one-hot encoding** on `ProductID`
- Creates a binary matrix (**Supplier × Product**) where:
  - `1` indicates the supplier sells the product
  - `0` indicates the supplier does not

---

### Distance Metric
- Uses **Jaccard Distance**, calculated as:

\[
\text{Distance} = 1 - J(A, B)
\]

Where \( J(A, B) \) is the **Jaccard Index**, defined as the size of the intersection divided by the size of the union of two product sets.

---

### Linkage Method
- Applies **Average Linkage** (`method="average"`)
- Clusters are merged using the average distance between all pairs of observations across the two clusters.
