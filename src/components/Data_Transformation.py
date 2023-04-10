import os
import sys
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass


@dataclass
class Data_Transformation_config:
    pass

class Data_Transformation_class:
    def get_data_transformation_object(self):
        
        categorical_cols = ['cut', 'color','clarity']
        numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']

        cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
        color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
        clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
        
        num_pipeline= Pipeline(
            steps= [
           ('SimpleImputer',SimpleImputer(strategy='median')),
            ('StandardScalar',StandardScaler())
        ]  
        )

        cat_pipeline= Pipeline(
            steps=[
            ('SimpleImputer',SimpleImputer(strategy='most_frequent')),
            ('OrdinalEncoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
            ('StandardScalar',StandardScaler())
        ]  
        )

        preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

        return preprocessor
    

    def initiate_data_transformation(self,Train_data_path,Test_data_path):
        train_df= pd.read_csv(Train_data_path)
        test_df= pd.read_csv(Test_data_path)

        drop_col=['Unnamed: 0']
        train_df.drop(drop_col,axis=1,inplace=True)
        test_df.drop(drop_col,axis=1,inplace=True)

        x_train = train_df.iloc[:,:-1]
        y_train = pd.DataFrame(train_df.iloc[:,-1])

        x_test = test_df.iloc[:,:-1]
        y_test= pd.DataFrame(test_df.iloc[:,-1])

        process= self.get_data_transformation_object()

       
        x_train=process.fit_transform(x_train)
        x_test=process.transform(x_test)

        # print(x_train.head())
        # print(y_train.head())

        # print(x_test.head())
        # print(y_test.head())

        return x_train,x_test,y_train,y_test


