# CDAC_Project
Project on US_Accident_Analysis 

Inspiration of our project is to do deep analysis of accident hotspot locations and to predict the accident rate and their severity in various weather conditions,time at which maximum accidents took place.
Various machine learning algorithms including Logistics,Naive Bayes,Light GBM Classifier,etc. have been applied.
However, the majority of studies on traffic accident analysis and prediction have used small-scale datasets with limited coverage, which limits their impact and applicability; and existing large-scale datasets are either private, old, or do not include important contextual information such as environmental stimuli (weather, points-of-interest, etc.).
In order to help the research community address these shortcomings we have - through a comprehensive process of data collection, integration, and augmentation – used a large-scale publicly available dataset of accident information named US-Accidents.

# Objective
To identify the severity of accidents based on weather conditions.
To identify the severity of accidents based on location.
To identify the severity of accidents based on type of road.
This analysis will be helpful for handle the challenging accident records situation in USA.

# Machine learning
Machine Learning is a concept which allows the machine to learn from examples and experience.
Machine Learning algorithm is trained using a training data set to create a model. When new input data is introduced to the ML algorithm, it makes a prediction on the basis of the model.
Types of machine learning
Supervised Learning
Unsupervised Learning
Reinforcement Learning
As in this project dependent or response variable is a categorical quantity we have to use classification techniques to achieve results.

Classification
Classification is a supervised learning approach in which the computer program learns from the data input given to it and then uses this learning to classify new observation.
Classification is nothing but classifying the forthcoming test sample dataset into distinct classes.
Some of the classification algorithms used in this project are
Logistic Regression
Multinomial Naive Bayes Classifier
Bernoulli Naive Bayes Classifier
XGBoost Classifier
LightGBM Classifier


1.Logistic Regression
Logistic Regression is a classification algorithm. It is used to predict a binary outcome (1 / 0, Yes / No, True / False) given a set of independent variables. To represent binary/categorical outcome, we use dummy variables. You can also think of logistic regression as a special case of linear regression when the outcome variable is categorical, where we are using log of odds as dependent variable. it predicts the probability of occurrence of an event by fitting data to a logit function.It’s a classification algorithm, that is used where the response variable Is categorical. The idea of Logistic Regression is to find a relationship between features and probability of particular outcome.

2.Naive Bayes Classifier
BernouliNB  implements the naive Bayes training and classification algorithms for data that is distributed according to multivariate Bernoulli distributions; i.e., there may be multiple features but each one is assumed to be a binary-valued (Bernoulli, boolean) variable. Therefore, this class requires samples to be represented as binary-valued feature vectors; if handed any other kind of data, a BernoulliNB instance may binarize its input (depending on the binarize parameter)

MultinomialNB implements the naive Bayes algorithm for multinomially distributed data, and is one of the two classic naive Bayes variants used in text classification (where the data are typically represented as word vector counts, although tf-idf vectors are also known to work well in practice). The distribution is parametrized by vectors 0y=(0y1,,……..,0yn) for each class , where is the number of features (in text classification, the size of the vocabulary) and 0yi is the probability P(xi|y)of feature appearing in a sample belonging to class y.

3.XGBoost Classifier
XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way.
XGBoost is an implementation of Gradient Boosted decision trees. This library was written in C++. It is a type of Software library that was designed basically to improve speed and model performance. It has recently been dominating in applied machine learning. XGBoost models majorly dominate in many Kaggle Competitions.
In this algorithm, decision trees are created in sequential form. Weights play an important role in XGBoost. Weights are assigned to all the independent variables which are then fed into the decision tree which predicts results. Weight of variables predicted wrong by the tree is increased and these the variables are then fed to the second decision tree. These individual classifiers/predictors then ensemble to give a strong and more precise model. It can work on regression, classification, ranking, and user-defined prediction problems.

4.LightGBM Classifier
Light GBM is a fast, distributed, high-performance gradient boosting framework based on decision tree algorithm, used for ranking, classification and many other machine learning tasks.LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with the following advantages :
Faster training speed and higher efficiency.
Lower memory usage.
Better accuracy.
Support of parallel and GPU learning.
Capable of handling large-scale data.

# Implementing Machine learning for Accident  Analysis
From this feature vector 30% of data is used for test or evaluation phase & rest of the data i.e. is used for training phase.
To test performance of model confusion matrix is calculated which will give us relation between Actual & Predicted values.
Accuracy is calculated as the total number of two correct predictions (TP + TN) divided by the total number of a dataset.







