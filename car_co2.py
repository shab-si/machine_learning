import pandas
from sklearn import linear_model

df = pandas.read_csv("Car_data.csv")

X = df[['Weight', 'Volume']]  # دو متغیر مستقل
y = df['CO2']  # متغیر وابسته یا پاسخ


# مدلسازی
regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

#We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.
print("predicted CO2: ", predictedCO2)
oldpredictedCO2 = predictedCO2

#These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
#And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
print("regression coeficience: ",regr.coef_)
print("predicted.x CO2: ", regr.coef_[0])
print("predicted.y CO2: ", regr.coef_[1])

#What if we increase the weight with 1000kg?

predictedCO2 = regr.predict([[3300, 1300]])

print("predicted CO2: ", predictedCO2)

# rah hal dovom
predictedCO2 = oldpredictedCO2 + (1000 * regr.coef_[0])
print("predicted CO2: ", predictedCO2)