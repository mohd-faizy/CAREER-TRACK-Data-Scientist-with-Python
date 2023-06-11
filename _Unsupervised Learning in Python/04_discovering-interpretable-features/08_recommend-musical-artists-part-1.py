'''
08 - Recommend musical artists part I

In this exercise and the next, you'll use what you've  learned about NMF  to 
recommend popular music artists! You are given a sparse array artists  whose 
rows correspond to artists and whose column correspond to users. The entries 
give the number of times each artist was listened to by each user.

In this exercise, build a pipeline and transform the array into normalized NMF 
features. The first step in the pipeline, MaxAbsScaler, transforms the data so 
that all users have the same influence on the model, regardless  of  how  many 
diff-erent artists they've listened to. In the next exercise, you'll  use  the 
resulting normalized NMF features for recommendation!

This data is part of a larger dataset available here.

INSTRUCTIONS

-Import:
- NMF from sklearn.decomposition.
    - Normalizer and MaxAbsScaler from sklearn.preprocessing.
    - make_pipeline from sklearn.pipeline.
    - Create an instance of MaxAbsScaler called scaler.

- Create an NMF instance with 20 components called nmf.
- Create an instance of Normalizer called normalizer.
- Create a pipeline called pipeline that chains together scaler, nmf, and normalizer.
- Apply the .fit_transform() method of pipeline to artists. Assign the result to norm_features.
'''
# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)

'''
Notes:
---------------------------------------------------------------
`MaxAbsScaler()`:

Scale each feature by its maximum absolute value.This estimator 
scales and translates each feature individually such  that  the 
maximal absolute value of each feature in the training set will 
be 1.0. It does not shift/center the data, and thus does not 
destroy any sparsity.
---------------------------------------------------------------
Use StandardScaler if you know the data distribution  is normal.
Many machine learning algorithms perform better  when  numerical 
input variables are scaled to a standard range. Scaling the data
means it helps to Normalize the data within a particular range.
---------------------------------------------------------------
'''
