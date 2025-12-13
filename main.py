from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import matplotlib.pyplot as plt

#--------------------------
# Read your Excel file
#--------------------------
file_path = r"dataset2.xlsx"
df = pd.read_excel(file_path)

#--------------------------
# One-hot encode ProductID
#--------------------------
df_encoded = pd.get_dummies(df, columns=["ProductID"])

# Build Supplier × Product matrix
supplier_product_matrix = df_encoded.groupby("SupplierID").max()

# Convert to NumPy matrix
X = supplier_product_matrix.values

#--------------------------
# Compute Jaccard distance
# pdist returns the condensed distance matrix
#--------------------------
jaccard_dist = pdist(X, metric="jaccard")

#--------------------------
# Hierarchical clustering using the distance matrix
#--------------------------
Z = linkage(jaccard_dist, method="average")   # recommended for Jaccard

#--------------------------
# Plot dendrogram,
#--------------------------
plt.figure(figsize=(12, 6))
dendrogram(
    Z,
    labels=supplier_product_matrix.index.astype(str),
    leaf_rotation=90
)
plt.title("Hierarchical Agglomerative Clustering (Jaccard Distance - Average Linkage)")
plt.xlabel("Supplier")
plt.ylabel("Distance")
plt.tight_layout()
plt.savefig('dendrogram.png', bbox_inches='tight')
