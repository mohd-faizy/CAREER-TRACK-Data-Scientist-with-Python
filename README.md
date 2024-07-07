[![author](https://img.shields.io/badge/author-mohd--faizy-red)](https://github.com/mohd-faizy)
![made-with-Markdown](https://img.shields.io/badge/Made%20with-markdown-blue)
![Language](https://img.shields.io/github/languages/top/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)
![Platform](https://img.shields.io/badge/platform-jupyter%20labs-blue)
![Maintained](https://img.shields.io/maintenance/yes/2024)
![Last Commit](https://img.shields.io/github/last-commit/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)
[![GitHub issues](https://img.shields.io/github/issues/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)](https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)
![Stars GitHub](https://img.shields.io/github/stars/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)
![Size](https://img.shields.io/github/repo-size/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python)


<p align='center'>
  <a href="#">
    <img src='https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/blob/main/_png/head_new.gif?raw=true' alt="head_image">
  </a>
</p>

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
libraries = [
    "NumPy", "Pandas", "Matplotlib", "Seaborn", "SciPy", "Scikit-learn", "TensorFlow", "Keras",
    "PyTorch", "Statsmodels", "XGBoost", "LightGBM", "CatBoost", "NLTK", "SpaCy", "Gensim",
    "Plotly", "Bokeh", "Dash", "H2O.ai", "PyCaret", "Dask", "Orange3"
]

# Parameters for circular layout
num_libs = len(libraries)
angles = np.linspace(0, 2 * np.pi, num_libs, endpoint=False).tolist()

# Plot
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': 'polar'})
bars = ax.bar(angles, np.ones(num_libs), width=0.3, bottom=2.5, color='skyblue', edgecolor='black')

# Add library names and URLs
for bar, angle, lib in zip(bars, angles, libraries):
    rotation = np.rad2deg(angle)
    alignment = 'left' if angle < np.pi else 'right'
    ax.text(angle, bar.get_height() + 3.0, lib, rotation=rotation, ha=alignment, va='center', fontsize=12, color='black')

# Customize plot
ax.set_yticklabels([])
ax.set_xticks([])
ax.spines['polar'].set_visible(False)
plt.show()

# Output
```
<p align='center'>
  <a href='#'>
    <img src='_png\dataScience.png' width=70%>
  </a>
</p>


# Data Science Repository

Welcome to the Data Science Repository! This repository is designed to help you learn Python for data science and develop the essential skills needed to succeed as a data scientist. From data manipulation to machine learning, you'll gain the knowledge required to excel in this field.

## Track Overview

This track is a comprehensive journey through Python for data science. It consists of various libraries and tools to import, clean, manipulate, visualize data, and build predictive models. Here's an overview of the contents in this repository:

# ➤ ⭐Python Essentials

| # | Project | Link |
|---|---------|------|
| 1 | **Introduction to Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/01_Introduction%20to%20Python" target="_blank"><button>Open</button></a> |
| 2 | **Intermediate Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/02_Intermediate%20Python" target="_blank"><button>Open</button></a> |


# ➤ ⭐Data Manipulation and Visualization

| # | Project | Link |
|---|---------|------|
| 1 | **Data Manipulation with pandas** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/03_Data%20Manipulation%20with%20pandas" target="_blank"><button>Open</button></a> |
| 2 | **Joining Data with pandas** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/04_Joining%20Data%20with%20pandas" target="_blank"><button>Open</button></a> |
| 3 | **Introduction to Statistics in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/05_Introduction%20to%20Statistics%20in%20Python" target="_blank"><button>Open</button></a> |
| 4 | **Introduction to Data Visualization with Matplotlib** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/06_Introduction%20to%20Data%20Visualization%20with%20Matplotlib" target="_blank"><button>Open</button></a> |
| 5 | **Introduction to Data Visualization with Seaborn** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/07_Introduction%20to%20Data%20Visualization%20with%20Seaborn" target="_blank"><button>Open</button></a> |
| 6 | **Python-data-science-toolbox-(part-1)** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/08_Python-data-science-toolbox-(part-1)" target="_blank"><button>Open</button></a> |
| 7 | **Python-data-science-toolbox-(part-2)** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/09_Python-data-science-toolbox-(part-2)" target="_blank"><button>Open</button></a> |
| 8 | **Intermediate Data Visualization with Seaborn** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/10_Intermediate%20Data%20Visualization%20with%20Seaborn" target="_blank"><button>Open</button></a> |


# ➤ ⭐ Exploratory Data Analysis (EDA) and Statistics

| # | Project | Link |
|---|---------|------|
| 1 | **Exploratory Data Analysis in Python Part - 1** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/11_A_Exploratory%20Data%20Analysis%20in%20Python" target="_blank"><button>Open</button></a> |
| 2 | **Exploratory Data Analysis in Python Part - 2** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/11_B__Exploratory%20Data%20Analysis%20in%20Python" target="_blank"><button>Open</button></a> |
| 3 | **Working with Categorical Data in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/12_Working_with_Categorical_Data_in_Python" target="_blank"><button>Open</button></a> |
| 4 | **Data Communication Concepts** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/13_Data_Communication_Conceptss" target="_blank"><button>Open</button></a> |


# ➤ ⭐ Data Importing and Cleaning

| # | Project | Link |
|---|---------|------|
| 1 | **Introduction to Importing Data in Python-(part-1)** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/14_Introduction%20to%20Importing%20Data%20in%20Python-(part-1)" target="_blank"><button>Open</button></a> |
| 2 | **Intermediate Importing Data in Python-(part-2)** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/15_Intermediate%20Importing%20Data%20in%20Python-(part-2)" target="_blank"><button>Open</button></a> |
| 3 | **Cleaning Data in Python [Part - 1]** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/16_Cleaning%20Data%20in%20Python%20%5BPart%20-%201%5D" target="_blank"><button>Open</button></a> |
| 4 | **Cleaning Data in Python [Part - 2]** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/17_Cleaning%20Data%20in%20Python%20%5BPart%20-%202%5D" target="_blank"><button>Open</button></a> |
| 5 | **Working with Dates and Times in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/18_Working%20with%20Dates%20and%20Times%20in%20Python" target="_blank"><button>Open</button></a> |


# ➤ ⭐ Advanced Topics

| # | Project | Link |
|---|---------|------|
| 1  | **Writing Functions in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/19_Writing%20Functions%20in%20Python" target="_blank"><button>Open</button></a> |
| 2  | **Introduction to Regression with statsmodels in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/20_Introduction_to_Regression_with_statsmodels_in_Python" target="_blank"><button>Open</button></a> |
| 3  | **Sampling in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/21_Sampling_in_Python" target="_blank"><button>Open</button></a> |
| 4  | **Hypothesis Testing in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/22_A_Hypothesis_Testing_in_Python" target="_blank"><button>Open</button></a> |
| 5  | **Statistical-Thinking-in-Python-[Part -1]** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/22_B_Statistical-Thinking-in-Python-%5BPart%20-1%5D" target="_blank"><button>Open</button></a> |
| 6  | **Statistical-Thinking-in-Python-[Part -2]** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/22_C_Statistical-Thinking-in-Python-%5BPart%20-2%5D" target="_blank"><button>Open</button></a> |
| 7  | **Supervised Learning with scikit-learn** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/23_Supervised%20Learning%20with%20scikit-learn" target="_blank"><button>Open</button></a> |
| 8  | **Unsupervised Learning in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/24_Unsupervised_Learning_in_Python" target="_blank"><button>Open</button></a> |
| 9  | **Cluster Analysis in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/25_%2B_Cluster-Analysis-in-Python" target="_blank"><button>Open</button></a> |
| 10  | **Machine Learning with Tree-Based Models in Python** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/25_Machine-Learning-with-Tree-Based-Models-in-Python" target="_blank"><button>Open</button></a> |
| 11  | **Preprocessing for Machine Learning** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/26_Preprocessing_for_Machine_Learning" target="_blank"><button>Open</button></a> |
| 12 | **Developing Python Packages** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/27_Developing_Python_Packages" target="_blank"><button>Open</button></a> |
| 13 | **Machine Learning for Business** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/28_Machine_Learning_for_Business" target="_blank"><button>Open</button></a> |
| 14 | **Introduction to SQL** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/29_Introduction_to_SQL" target="_blank"><button>Open</button></a> |
| 15 | **Intermediate SQL** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/30_Intermediate_SQL" target="_blank"><button>Open</button></a> |
| 16 | **Joining Data in SQL** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/31_Joining_Data_in_SQL" target="_blank"><button>Open</button></a> |
| 17 | **Introduction to Git** | <a href="https://github.com/mohd-faizy/CAREER-TRACK-Data-Scientist-with-Python/tree/main/32_Introduction_to_Git" target="_blank"><button>Open</button></a> |



# ➤ ⭐ Projects

In addition to the comprehensive learning materials, this repository offers various projects to apply and reinforce your data science skills. Here is a list of the projects available:

| # | Project | Link |
|---|---------|------|
| 1 | **Analyzing TV Data** |  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1r91R2HXnkr5wBm-7_R3hVXI1ouTa5rAT?authuser=1)|
| 2 | **Investigating Netflix Movies** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DIPVZ483Q8M1DzygIpXJOIcskm_ld391?authuser=1) |
| 3 | **What and Where are the World's Oldest Businesses** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FtmNWsky8S1h9WAb35tpvztAkoHipcNJ?authuser=1) |
| 4 | **Google Play Store Apps and Reviews** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nrdDlME9722A0Ui2hAqZcl1HgUkBMVbz?authuser=1) |
| 5 | **The GitHub History of the Scala Language** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qbskfw477wOMOq8sd48qSOCaXJwna3Hd?authuser=1)  |
| 6 | **A Visual History of Nobel Prize Winners** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16yAqJurdNSEh4UBmUQ4x77aiDjZTguvN?authuser=1)   |
| 7 | **Dr. Semmelweis and the Discovery of Handwashing** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gSSLGEXelnffjc927cPq5MBKdVFver6X?authuser=1)  |
| 8 | **Predicting Credit Card Approvals** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1YPmHiweI6dgGpzbSGqnRczt0E6WDZMkL?authuser=1)  |
| 9 | **School Budgeting with Machine Learning in Python** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mAYturGFpKFGv-okj4Fxd_WCVLNaZBs6?authuser=1)  |
| 10 | **Analyzing Police Activity with pandas** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1YxH9LWKJ--0xH1pYIIdO7aWui0cRkvll?authuser=1)   |
| 11 | **Exploring NYC Public School Test Result Scores** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/198mJ0l8HaFXIWMVXaeTggLpi4FtviZDe?authuser=1)|
| 12 | **Analyzing Crime in Los Angeles** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16kWK8G8XX1FYOlkwg8_JClHbjSl4rpm3?authuser=1)  |
| 13 | **Preparing Data for Customer Analytics Modeling** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AKp7nDs5VN36bjg5okh17rIYRqXDfB0q?authuser=1) |
| 14 | **Modeling Car Insurance Claim Outcomes(EDA)** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PyXGUyLxQZ0WiTMh840MP0_T7pOlmtyr?authuser=1) |
|  | **Modeling Car Insurance Claim Outcomes(ML)** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zwklSBB97TAfZP1N-cn-EmTGeEZayqsl?authuser=1)|
|  | **Modeling Car Insurance Claim Outcomes(GB-RF)** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mnJtBcE-yd9Kp34jRvb1fY0Ni_SgEaCL?authuser=1)|
|  | **Modeling Car Insurance Claim Outcomes(Ensemble_Method)** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qhBDuPr46Wa3UD7N7vc8Rf1yymYqiWQk?authuser=1)|
| 15 | **Hypothesis Testing Soccer Matches** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bL2ng1xzVb6D1WGxutVjLXQU3Fb-Ooxj?authuser=1)|
| 16 | **Predictive Modeling for Agriculture** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16MjYL_CC_ZHBNQMW8XeHfwZQvy5vHtzt?authuser=1)|
| 17 | **Clustering Antarctic Penguin Species**  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tkbeIGedkQpU4Zv4B2gz_gsBfLCwvPd0?authuser=1)|
| 18 | **Predicting Movie Rental Durations**  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]()|
| 19 | 🔜  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15M5RgV-f8Fyl6Cm-UhrtphYKWuHkM6MB?authuser=1)  |




# 🗂️ ➤ Additional Resources

- ➤ [**Python**](https://github.com/mohd-faizy/learn_python)
- ➤ [**Machine Learning**](https://github.com/mohd-faizy/Machine-Learning-Scientist-with-Python)
- ➤ [**Machines leaning and Data science in one Notebook**](https://github.com/mohd-faizy/ML-DS-OneNote)
- ➤ [**Feature Engineering & Feature selection**](https://github.com/mohd-faizy/feature-engineering-hacks)
- ➤ [**Statistics for Data Science**](https://github.com/mohd-faizy/Stats-with-Data)
- ➤ [**Data Preprocessing**](https://github.com/mohd-faizy/Preprocess_ML)
- ➤ [**NumPy**](https://github.com/mohd-faizy/Learn_Numpy)
- ➤ [**Matplotlib**](https://github.com/mohd-faizy/Learn_Matplotlib)
- ➤ [**Pandas**](https://github.com/mohd-faizy/Learn_Pandas)
- ➤ [**Seaborn**](https://github.com/mohd-faizy/Learn_Seaborn)


## ⭐ **RoadMap OLD**

<p align='center'>
  <a href="#">
    <img src='_png\Data-Scientist with-Python.jpg' alt="map_img">
  </a>
</p>

## 📊📈📉 **STATISTICS** 

<p align='center'>
  <a href="#">
    <img src='_png\STATISTICS.jpg' alt="map_img">
  </a>
</p>



---

## 📄 ➤ STATEMENT OF ACCOMPLISHMENT

➤ ⭐[1. **Data Scientist Professional with Python**](https://www.datacamp.com/statement-of-accomplishment/track/4f083548e0a1ba78080f3b8734b3d6e37b58d197?raw=1)


<p align='center'>
  <a href='https://www.datacamp.com/statement-of-accomplishment/track/4f083548e0a1ba78080f3b8734b3d6e37b58d197?raw=1'>
    <img src='_Certificates\Data Scientist Professional with Python.jpg' width=70%>
  </a>
</p>

➤ ⭐[2. **Associate Data Scientist**](https://www.datacamp.com/statement-of-accomplishment/track/aa09804d27b7b3792c7f55c131373799d0675dbd?raw=1)
<p align='center'>
  <a href='https://www.datacamp.com/statement-of-accomplishment/track/aa09804d27b7b3792c7f55c131373799d0675dbd?raw=1'>
    <img src='_Certificates\Associate Data Scientist in Python.jpg' width=70%>
  </a>
</p>




## ⚖ ➤ License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## ❤️ ➤ Support

If you find this repository helpful, show your support by starring it! For questions or feedback, reach out on [Twitter(`X`)](https://twitter.com/F4izy).

#### $\color{skyblue}{\textbf{Connect with me:}}$

🔃 ➤ If you have questions or feedback, feel free to reach out!!!

[<img align="left" src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/twitter_circle-512.png" width="32px"/>][twitter]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="32px"/>][linkedin]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/2626/2626299.png" width="32px"/>][Portfolio]

[twitter]: https://twitter.com/F4izy
[linkedin]: https://www.linkedin.com/in/mohd-faizy/
[Portfolio]: https://ai.stackexchange.com/users/36737/faizy?tab=profile

---

<img src="https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true" width=380px height=200px />
