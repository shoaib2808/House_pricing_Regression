import os
import sys
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import pickle


def evaluate_model(self,y_pred,y_test):
        r2=r2_score(y_pred,y_test)
        mae=mean_absolute_error(y_pred,y_test)
        mse=mean_squared_error(y_pred,y_test)
        return (r2,mse,mae)


def save_obj(obj,file_path):
        with open(file_path,"wb") as file_obj:
                pickle.dump(obj,file_obj)
