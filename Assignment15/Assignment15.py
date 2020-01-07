import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


def WinePredictor():
	file=pd.read_csv("WinePredictor.csv")
	#print(file)
	label=file.Class
	#print("Label is=",label)

	Alcohol=file.Alcohol
	label1=file.Malic_acid
	label2=file.Ash
	label3=file.Alcalinity_of_ash
	label4=file.Magnesium
	label5=file.Total_phenols
	label6=file.Flavanoids
	label7=file.Nonflavanoid_phenols
	label8=file.Proanthocyanins
	label9=file.Color_intensity
	label10=file.Hue
	label11=file.OD280OD315_of_diluted_wines
	label12=file.Proline

	data=data=list(zip(Alcohol,label1,label2,label3,label4,label5,label6,label7,label8,label9,label10,label11,label12))

	train_data,test_data,train_label,test_label=train_test_split(data,label,test_size=0.2)
	for i in range(len(test_label)):
		# print(test_label)
		i=i+1
	print("train size=",i)

	algo=KNeighborsClassifier()
	algo.fit(train_data,train_label)
	predict=algo.predict(test_data)

	accuracy=accuracy_score(test_label,predict)
	return accuracy

def main():
	print("*"*40)
	print("...Wine Predictor...")
	print("*"*40)

	ans=WinePredictor()
	print(ans*100)




if __name__=="__main__":
	main()



# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment15
# $ python Assignment15.py
# ****************************************
# ...Wine Predictor...
# ****************************************
# train size= 36
# 75.0

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment15
# $ python Assignment15.py
# ****************************************
# ...Wine Predictor...
# ****************************************
# train size= 36
# 80.55555555555556
