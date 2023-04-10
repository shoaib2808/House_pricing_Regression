import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from Data_Ingestion import Data_ingestion_class
from Data_Transformation import Data_Transformation_class
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
# from src.utils import evaluate_model
import pickle
from dataclasses import dataclass

@dataclass
class Model_Trainer_config:
    trained_model_file_path=os.path.join("Artifacts","bestModel.pkl")



class Model_Trainer:
    def __init__(self):
        self.model_file_path=Model_Trainer_config()

    def initiate_model_training(self,x_train,x_test,y_train,y_test):
        models={
            "LinearRegression":LinearRegression(),
            "Ridge":Ridge(),
            "Lasso":Lasso(),
            "ElasticNet":ElasticNet()
        }
        models_report=dict()
        for i in models.keys():
            print("="*30)
            print(i)
            regressor=models[i].fit(x_train,y_train)
            y_pred=regressor.predict(x_test)
            r2,mse,mae=self.evaluate_model(y_test,y_pred)
            models_report[i]=r2
            print(f"Model : {i}, r2_score : {r2}, mean squre error : {mse} , mean absolute error : {mae}")
            print("="*30)

        best_r2 = sorted(list(models_report.values()))[-1]
        best_model=''
        for i in models_report:
             if(models_report[i]==best_r2):
                best_model=i
                break
        print(f"Best model is {best_model}")
        best_model_obj=models[best_model]

        self.save_obj(best_model_obj,self.model_file_path.trained_model_file_path)




    def evaluate_model(self,y_pred,y_test):
        r2=r2_score(y_pred,y_test)
        mae=mean_absolute_error(y_pred,y_test)
        mse=mean_squared_error(y_pred,y_test)
        return (r2,mse,mae)

    def save_obj(self,obj,file_path):
        with open(file_path,"wb") as file_obj:
                pickle.dump(obj,file_obj)

if __name__ == "__main__":
   obj= Data_ingestion_class()
   Train_data_path,Test_data_path=obj.initiate_data_injestion()
   obj1= Data_Transformation_class()
   x_train,x_test,y_train,y_test=obj1.initiate_data_transformation(Train_data_path,Test_data_path)
   obj2=Model_Trainer()
   obj2.initiate_model_training(x_train,x_test,y_train,y_test)
