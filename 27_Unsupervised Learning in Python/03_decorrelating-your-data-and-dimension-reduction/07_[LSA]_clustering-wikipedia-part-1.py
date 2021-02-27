'''
07 - Clustering Wikipedia part I

You saw in the video that TruncatedSVD is able to perform PCA on sparse arrays 
in csr_matrix format, such as word-frequency arrays. Combine your knowledge of 
TruncatedSVD and k-means to cluster some popular pages from Wikipedia. In this 
exercise, build the pipeline. In the next exercise, you'll  apply  it  to  the 
word-frequency array of some Wikipedia articles.

Create a Pipeline object consisting of a TruncatedSVD followed by KMeans. (This 
time, we've precomputed the word-frequency matrix for you, so there's no need 
for a TfidfVectorizer).

The Wikipedia dataset you will be working with was obtained from here.
-----------------------------------------------------------------------------
Dimensionality reduction using `truncated SVD` (aka LSA).

This transformer performs linear dimensionality reduction by means of  truncated 
singular value decomposition (SVD). Contrary to  PCA, this  estimator  does  not 
center the data before computing the singular value decomposition. This means it 
can work with sparse matrices efficiently.

In particular, truncated SVD works on term count/tf-idf  matrices  as  returned  by 
the vectorizers in sklearn.feature_extraction.text. In that context, it is known as 
`latent semantic analysis (LSA)`.

This estimator supports two algorithms: a fast randomized SVD solver, and a "naive" 
algorithm that uses ARPACK as an eigensolver on X * X.T or X.T * X, whichever is more 
efficient.
------------------------------------------------------------------------------
Instructions

- Import:
    - TruncatedSVD from sklearn.decomposition.
    - KMeans from sklearn.cluster.
    - make_pipeline from sklearn.pipeline.

- Create a TruncatedSVD instance called svd with n_components=50.
- Create a KMeans instance called kmeans with n_clusters=6.
- Create a pipeline called pipeline consisting of svd and kmeans.
'''

# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)
