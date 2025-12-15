# High Dimensional Analysis

## Coded By: 
[Miguel Angel Pafalox Gomez](https://github.com/ter-kes) [Clustering]

[Bhavik Bhagat](https://bhavikbhagat.netlify.app) [Recified the SQL Query]

Md Chistia Chowdhury [Provided initial SQL Query]

## 1. Overview

This project performs high-dimensional analysis on supplier data with two main components:

**Part 1: Identify Overcharging Suppliers**  
Uses SQL queries to find suppliers whose unit costs exceed the average cost for each product.

**Part 2: Hierarchical Clustering for Supplier Alternatives**  
Performs hierarchical agglomerative clustering on supplier data based on their product portfolios to identify alternative suppliers.

The analysis uses the Jaccard Distance metric to quantify dissimilarity between suppliers and visualizes relationships using a dendrogram.

---

## 2. Dependencies

The scripts require the following Python packages:

- **pandas** — data loading and manipulation  
- **scipy** — distance calculation and hierarchical clustering  
  - `pdist`
  - `linkage`
- **matplotlib** — visualization (dendrogram plotting)  
- **openpyxl** — required by pandas to read `.xlsx` files  
- **sqlite3** — for in-memory database operations (standard library)  

---

## 3. Setup and Installation

This project uses **`uv`** for fast and isolated dependency management.

### A. Install `uv`

If `uv` is not already installed, install it using your terminal.

Reference: [uv documentation](https://docs.astral.sh/uv/getting-started/installation/)

Windows (after running the command, restart the terminal):
```bash
winget install astral-sh.uv
```

Linux/Mac:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### B. Clone the project from GitHub
```bash
git clone <url>
```

where url could be one of the following

normal-url: ```https://github.com/bhavik-knight/5560-high-dimensional-analysis.git```

ssh-url: ```git@github.com:bhavik-knight/5560-high-dimensional-analysis.git```

### C. Install dependencies
```bash
uv sync
```

---

## 4. Part 1: Find Overcharging Suppliers

### Execution
```bash
uv run query.py
```

### Description
This script reads supplier data from `Supplier_Cube_PivotTable_TT.xlsx`, loads it into an in-memory SQLite database, and executes a SQL query to identify suppliers charging above the average unit cost for each product.

### Output
Prints a DataFrame showing:
- Supplier First Name
- Product Name
- Unit Cost
- Average Unit Cost for the Product

Sorted by descending unit cost.

---

## 5. Part 2: Hierarchical Clustering Analysis

### Execution
```bash
uv run clustering.py
```

### Description
This script performs hierarchical agglomerative clustering on supplier data from `dataset2.xlsx` based on their product portfolios.

### Output
- Console Output: Prints messages during execution (if any).
- Visualization Output: A saved image file (`dendrogram.png`) displaying the hierarchical clustering dendrogram.

---

## 6. Core Logic Details

### Part 1: Query Logic
- Loads Excel sheets into pandas DataFrames and stores them in an SQLite database.
- Uses a CTE to calculate average unit costs per product.
- Joins back to find suppliers exceeding the average cost.

### Part 2: Clustering Logic

#### Data Preparation
- Performs **one-hot encoding** on `ProductID`
- Creates a binary matrix (**Supplier × Product**) where:
  - `1` indicates the supplier sells the product
  - `0` indicates the supplier does not

#### Distance Metric
- Uses **Jaccard Distance**, calculated as:

\[
\text{Distance} = 1 - J(A, B)
\]

Where \( J(A, B) \) is the **Jaccard Index**, defined as the size of the intersection divided by the size of the union of two product sets.

#### Linkage Method
- Applies **Average Linkage** (`method="average"`)
- Clusters are merged using the average distance between all pairs of observations across the two clusters.



