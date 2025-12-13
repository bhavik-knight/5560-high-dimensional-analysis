# Hierarchical Clustering Analysis

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

### 