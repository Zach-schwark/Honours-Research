from DataPreprocessing import DataPreprocessing
import pandas as pd


loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)

data.to_csv("Data/preprocessed_data.csv",index=False)

