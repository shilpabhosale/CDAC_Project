#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:46:23 2020

@author: student
"""
import pandas as pd
from selenium import webdriver
import tarfile
from hdfs import *
from hdfs import InsecureClient
from hdfs3 import HDFileSystem
from pyhive import hive
import sasl
import pandas as pd

from ETL_Task import ETLTask1 
#
#host_name = "localhost"
#port = 10000
#user = "hduser"
#password = "password"
#database = "default"
#conn = hive.Connection(host = host_name, port = port, database = database,username=user,auth="NOSASL")
#cur = conn.cursor()
class AccidentAlgorithm:
    def based_on_location():
        e1=ETLTask1
        e1.create_loc_table()
        
        x=df2.iloc[:,1:4].values
        y=df2.iloc[:,0:1].values
        
#        x['City']=pd.factorize(x['City'])[0]
#        x['State']=pd.factorize(x['State'])[0]
        from sklearn.feature_extraction.text import TfidfVectorizer
        df2['City'] = df2['City']
        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(df2['City'].values.astype('U'))
        print(vectorizer.get_feature_names())
        
        from sklearn.feature_extraction.text import TfidfVectorizer
        df2['State'] = df2['State']
        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(df2['State'].values.astype('U'))
        print(vectorizer.get_feature_names())
        
        from sklearn.feature_extraction.text import TfidfVectorizer
        df2['Street'] = df2['Street']
        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(df2['Street'].values.astype('U'))
        print(vectorizer.get_feature_names())      
        
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
        
        print("############################################################")
# Logistic classifier:
        from sklearn.linear_model import LogisticRegression
        classifier=LogisticRegression(random_state=0)
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        
        from sklearn.metrics import confusion_matrix
        cm1=confusion_matrix(y_test,y_pred)
        
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        l1=scores.mean()
        print("Average of Logistic Classifier",l1)
        
        from sklearn.metrics import accuracy_score
        print("Logistic Classifier",accuracy_score(y_test,y_pred))
        
        print("############################################################")
#Light GBM:              
        import lightgbm as ltb
        model = ltb.LGBMClassifier()
        model.fit(x_train, y_train)
        print(model)      
        expected_y  = y_test
        y_pred= model.predict(x_test)
        
        from sklearn.metrics import confusion_matrix
        cm2 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(model,x_train,y_train)
        ltb1=scores.mean()
        
        print("Average of Light GBM  Classifier",ltb1)
        from sklearn.metrics import accuracy_score
        print("Light GBM Classifier",accuracy_score(y_test,y_pred))
        
        print("############################################################")
#XGBoost Classifier:
        from xgboost import XGBClassifier
        from sklearn.metrics import accuracy_score
        classifier=XGBClassifier()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm3 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        xg1=scores.mean()
        print("XGBoostClassifier",accuracy_score(y_test,y_pred))
        print("XGBoostClassifie",xg1)
# MultinomialNB Naive Bayes:
        from sklearn.naive_bayes import MultinomialNB
        classifier=MultinomialNB()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm4 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        mlt1=scores.mean()
        print("Average of Naive Bayes Classifier",mlt1)
        from sklearn.metrics import accuracy_score
        print("Multinomial Naive Bayes Classifier",accuracy_score(y_test,y_pred))
        print("############################################################")        
        
        print("Location wise Accident Analysis Classification Report")
        pdict1={"Logistics Regression":l1,"Multinomial Naive Bayes Classifier":mlt1,"Light GBM Classifier":ltb1,"XGBoostClassifie":xg1}
        print(pdict1)
        for k,v in pdict1.items():
            if v==pdict1.get(max(pdict1,key=pdict1.get)):
                print(k, "---->",v,"\n")
                
    def based_on_road():
        e1=ETLTask1
        e1.createroadtable()             
        x=df1.iloc[:,1:15].values
        y=df1.iloc[:,0:1].values        
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        labelencoder_x=LabelEncoder()
        x[:,0]=labelencoder_x.fit_transform(x[:,0])
        x[:,1]=labelencoder_x.fit_transform(x[:,1])
        x[:,2]=labelencoder_x.fit_transform(x[:,2])
        x[:,3]=labelencoder_x.fit_transform(x[:,3])
        x[:,4]=labelencoder_x.fit_transform(x[:,4])
        x[:,5]=labelencoder_x.fit_transform(x[:,5])
        x[:,6]=labelencoder_x.fit_transform(x[:,6])
        x[:,7]=labelencoder_x.fit_transform(x[:,7])
        x[:,8]=labelencoder_x.fit_transform(x[:,8])
        x[:,9]=labelencoder_x.fit_transform(x[:,9])
        x[:,10]=labelencoder_x.fit_transform(x[:,10])
        x[:,11]=labelencoder_x.fit_transform(x[:,11])
        from sklearn.model_selection import train_test_split 
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
# Logistic classifier:
        from sklearn.linear_model import LogisticRegression
        classifier=LogisticRegression(random_state=0)
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
      
        from sklearn.metrics import confusion_matrix
        cm21=confusion_matrix(y_test,y_pred)
     
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        l2=scores.mean()
    
        print("Average of Logistic Classifier",l2)
        from sklearn.metrics import accuracy_score
        print("Logistic Classifier",accuracy_score(y_test,y_pred))
    
        print("############################################################")
# MultinomialNB Naive Bayes:
        from sklearn.naive_bayes import MultinomialNB
        classifier=MultinomialNB()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm22 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        mlt2=scores.mean()
        print("Average of Naive Bayes Classifier",mlt2)
        from sklearn.metrics import accuracy_score
        print("Multinomial Naive Bayes Classifier",accuracy_score(y_test,y_pred))
        print("############################################################")
#.Bernouli Naive Bayes:
        from sklearn.naive_bayes import BernoulliNB
        classifier=BernoulliNB()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm23 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        gs2=scores.mean()
        from sklearn.metrics import accuracy_score
        print("Bernouli Naive Bayes Classifier",accuracy_score(y_test,y_pred))
        print("Average of BernoulliNB Naive Bayes Classifier",gs2)
        print("############################################################")
#.LightGBM:    
        import lightgbm as ltb
        model = ltb.LGBMClassifier()
        model.fit(x_train, y_train)
        print(model)      
        expected_y  = y_test
        y_pred= model.predict(x_test)
    
        from sklearn.metrics import confusion_matrix
        cm24 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(model,x_train,y_train)
        ltb2=scores.mean()
        print("Average of Light GBM  Classifier",ltb2)
        from sklearn.metrics import accuracy_score
        print("Light GBM Classifier",accuracy_score(y_test,y_pred))
        print("############################################################")
        
        print("Road wise Accident Analysis Classification Report")
        pdict2={"Logistics Regression":l2,"BernoulliNB Naive Bayes Classifier":gs2,"Multinomial NB Classifier":mlt2,"Light gbm Classifier":ltb2}
        print(pdict2)
        for k,v in pdict2.items():
            if v==pdict2.get(max(pdict2,key=pdict2.get)):
                print(k, "---->",v,"\n")
          
    def based_on_weather():
        e1=ETLTask1
        e1.create_weather_table()   
        
        x=df3.iloc[:,1:8].values
        y=df3.iloc[:,0:1].values
        
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        labelencoder_x=LabelEncoder()
        x[:,6]=labelencoder_x.fit_transform(x[:,6])
       
        #print(x[:,6])
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

        from sklearn.feature_extraction.text import TfidfVectorizer
        df3['Weather_Condition'] = df3['Weather_Condition']
        vectorizer = TfidfVectorizer()
        x = vectorizer.fit_transform(df3['Weather_Condition'].values.astype('U'))
        print(vectorizer.get_feature_names())
# Logistic classifier:
        from sklearn.linear_model import LogisticRegression
        classifier=LogisticRegression(random_state=0)
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        
        from sklearn.metrics import confusion_matrix
        cm31=confusion_matrix(y_test,y_pred)
        
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        l3=scores.mean()
        print("Average of Logistic Classifier",l3)
        from sklearn.metrics import accuracy_score
        print("Logistic Classifier",accuracy_score(y_test,y_pred)) 
        print("############################################################")
#.Bernouli Naive Bayes:
        from sklearn.naive_bayes import BernoulliNB
        classifier=BernoulliNB()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm32 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        gs3=scores.mean()
        print("Average of BernoulliNB Naive Bayes Classifier",gs3)
        from sklearn.metrics import accuracy_score
        print("Bernouli Naive Bayes Classifier",accuracy_score(y_test,y_pred))
        print("############################################################")
#Light GBM:       
        import lightgbm as ltb
        model = ltb.LGBMClassifier()
        model.fit(x_train, y_train)
        print(model)      
        expected_y  = y_test
        y_pred= model.predict(x_test)
        
        from sklearn.metrics import confusion_matrix
        cm33 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(model,x_train,y_train)
        ltb3=scores.mean() 
        print("Average of Light GBM  Classifier",ltb3)
        from sklearn.metrics import accuracy_score
        print("Light GBM Classifier",accuracy_score(y_test,y_pred))
#XGBoost Classifier:
        from xgboost import XGBClassifier
        from sklearn.metrics import accuracy_score
        classifier=XGBClassifier()
        classifier.fit(x_train,y_train)
        y_pred=classifier.predict(x_test)
        from sklearn.metrics import confusion_matrix
        cm34 = confusion_matrix(y_test,y_pred)
        from sklearn.model_selection import cross_val_score
        scores=cross_val_score(classifier,x_train,y_train)
        xg3=scores.mean()
        print("Average of XGBoostClassifier",xg3)
        from sklearn.metrics import accuracy_score
        print("XGBoostClassifier",accuracy_score(y_test,y_pred))
        
        
        print("Weather wise Accident Analysis Classification Report")
        pdict3={"Logistics Regression":l3,"BernoulliNB Naive Bayes Classifier":gs3,"Light GBM  Classifier":ltb3,"XGBoostClassifie":xg3}
        print(pdict3)
        for k,v in pdict3.items():
            if v==pdict3.get(max(pdict3,key=pdict3.get)):
                print(k, "---->",v,"\n")
def main_mthd():               
    obj1= AccidentAlgorithm
    obj1.based_on_weather()
    obj1.based_on_location()
    obj1.based_on_road()
main_mthd()    
