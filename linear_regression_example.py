import matplotlib.pyplot as plt
from scipy import stats

x = [1.5,2,5,2.5,6,3,8,4.5,5,6]   #studing hours
y = [14,15,17.5,16,18,16,20,17,19,19]   #scores

slope, intercept, r, p, std_err = stats.linregress(x, y)

print("r =" , r)

def myfunc(x):  
  return slope * x + intercept 
  
mymodel = list(map(myfunc, x))  
plt.scatter(x, y)      
plt.plot(x, mymodel)  
plt.show()
print("a")

score = myfunc(7.5)

print(score)
x.append(7.5)  
y.append(score) 
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("New r =" , r)
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
