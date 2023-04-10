import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class Data_ingestion_config:
    train_data_path:str = os.path.join('Artifacts',"Train.csv")
    test_data_path:str = os.path.join('Artifacts',"Test.csv")
    raw_data_path:str = os.path.join('Artifacts',"Raw.csv")

class Data_ingestion_class:
    def __init__(self):
        self.ingestion_config=Data_ingestion_config()

    
    def initiate_data_injestion(self):
        df=pd.read_csv("Notebooks\Data\Gemstone.csv")

        df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

        train_data,test_data=train_test_split(df,test_size=0.30,random_state=34)


        train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

        test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

        return(
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path,
        )
    
