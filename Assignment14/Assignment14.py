
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()


def wather():

	f_data=pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")
	

	wather=f_data.Wether
	temp=f_data.Temperature
	play=f_data.Play

	temp=le.fit_transform(temp)
	wather=le.fit_transform(wather)
	label=le.fit_transform(play)

	data=list(zip(temp,wather))

	data_train,data_test,target_train,target_test=train_test_split(data,label,test_size=0.5)

	algo=KNeighborsClassifier()

	algo.fit(data_train,target_train)
	predict=algo.predict(data_test)
	
	print("-"*70)
	print("Expected Output",target_test)
	print("*"*70)
	print("Actual Result  ",predict)
	print("-"*70)

	accuracy=accuracy_score(target_test,predict)

	return accuracy
	
	

def main():
	print("-"*70)
	print(".....Wather Analysis.....")
	print("-"*70)

	ans=wather()
	print("Accuracy=",ans*100)


if __name__=="__main__":
	main()



# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment14
# $ python Assignment14.py
# ----------------------------------------------------------------------
# .....Wather Analysis.....
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Expected Output [0 1 1 0 1 1 1 1 1 1 0 1 0 0 1 1 0 0 1 0]
# **********************************************************************
# Actual Result   [0 1 1 0 0 1 1 1 1 1 1 1 0 0 1 1 1 1 1 0]
# ----------------------------------------------------------------------
# zale na bhava= 80.0

