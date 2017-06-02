# Customer Engagement, Campaign Performance, and Resource Efficiency

Unsupervised learning techniques applied on product spending data collected for customers of a wholesale distributor in Lisbon, Portugal to identify customer segments hidden in the data. 

- Explore the data by selecting a small subset to sample and determine if any product categories highly correlate with one another. 
- Preprocess the data by scaling each product category and then identifying (and removing) unwanted outliers. 
- With the good, clean customer spending data, apply PCA transformations to the data and implement clustering algorithms to segment the transformed customer data. 
- Finally, compare the segmentation found with an additional labeling and consider ways this information could assist the wholesale distributor with future service changes.

Success Story: 
JJ Food Service
Food Delivery Service Uses Machine Learning to Revolutionize Customer Service
https://customers.microsoft.com/Pages/CustomerStory.aspx?recid=12792 


Instructions: 
# Project 3: Unsupervised Learning
## Creating Customer Segments

### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

### Code

Template code is provided in the notebook `customer_segments.ipynb` notebook file. Additional supporting code can be found in `renders.py`. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project.

### Run

In a terminal or command window, navigate to the top-level project directory `creating_customer_segments/` (that contains this README) and run one of the following commands:

```ipython notebook customer_segments.ipynb```
```jupyter notebook customer_segments.ipynb```

This will open the iPython Notebook software and project file in your browser.

## Data

The dataset used in this project is included as `customers.csv`. You can find more information on this dataset on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers) page.
