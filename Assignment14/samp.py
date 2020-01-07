from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

train = ["paris", "paris", "tokyo", "amsterdam"]
test = ["tokyo", "paris","amsterdam"]

b=le.fit(['train'])
print ("b=",b)
a=le.transform(['test'])
print(train)
print(a)