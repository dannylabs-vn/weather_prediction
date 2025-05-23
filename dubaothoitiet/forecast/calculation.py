import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def process_inputs(inputs):
	result = 1
	new_input = [
	    inputs[0],
	    float(inputs[1]),
	    float(inputs[2]),
	    float(inputs[3]),
	    float(inputs[4])
	]
	
	df3 = pd.read_csv("dataset.csv")
	df_numeric = df3.select_dtypes(include=[np.number])
	Q1 = df_numeric.quantile(0.25)
	Q3 = df_numeric.quantile(0.75)
	IQR = Q3 - Q1
	df3 = df3[~((df_numeric < (Q1 - 1.5 * IQR)) | (df_numeric > (Q3 + 1.5 * IQR))).any(axis=1)]

	df3["precipitation"] = np.sqrt(df3["precipitation"])
	df3["wind"] = np.sqrt(df3["wind"])
	lc = LabelEncoder()
	df3["weather"] = lc.fit_transform(df3["weather"])
	df3["date"] = pd.to_datetime(df3["date"])
	df3["date"] = df3["date"].apply(lambda x: int(x.timestamp()))
	x_df3 = df3.loc[:, df3.columns != "weather"].astype(np.int64).values
	y_df3 = df3["weather"].values
	x_train_df3, x_test_df3, y_train_df3, y_test_df3 = train_test_split(x_df3, y_df3, test_size=0.1, random_state=2)
	dec_df3 = DecisionTreeClassifier(max_depth=4, max_leaf_nodes=15, random_state=0)
	dec_df3.fit(x_train_df3, y_train_df3)
	df_new = pd.DataFrame([new_input], columns=["date", "precipitation", "high_temperature", "low_temperature", "wind"])

	#df_new = df_new[~((df_new < (Q1 - 1.5 * IQR)) | (df_new > (Q3 + 1.5 * IQR))).any(axis=1)]

	df_new["precipitation"] = np.sqrt(df_new["precipitation"])
	df_new["wind"] = np.sqrt(df_new["wind"])
	df_new["date"] = pd.to_datetime(df_new["date"])
	df_new["date"] = df_new["date"].apply(lambda x: int(x.timestamp()))
	x_new = df_new.loc[:, df_new.columns != "weather"].astype(np.int64).values
	predictions = dec_df3.predict(x_new)
	predicted_weather = lc.inverse_transform(predictions)
	result= predicted_weather[0]

	

	return result

