print("test")
import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86, 93,102,85,101]
print(speed)
x = numpy.mean(speed)
print("mean: ", x)

x = numpy.median(speed)
print("median: ",x)

x = stats.mode(speed)
print("mode: ", x)

x = numpy.std(speed)
print("standard deviation: ", x)  # هر چقدر نزدیک به صفر باشد یعنی به میانگین نزدیکتر است و ژراکندگی کمتر است

x = numpy.var(speed)
print("variance: ", x)  #بیشترین میزان پراکنذگی در چه نقطه ای است؟


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(ages)
x = numpy.percentile(ages, 75) # سوال میگه که 75 درصد اعداد زیر چه سنی هستند؟
print("lower than this age: ", x)


x = numpy.random.uniform(0.0, 5.0, 250)
y = numpy.median(x)
print("median: ",y)
y = numpy.std(x)
print("standard deviation: ", y)  # هر چقدر نزدیک به صفر باشد یعنی به میانگین نزدیکتر است و ژراکندگی کمتر است
y = numpy.var(x)
print("variance: ", y)  #بیشترین میزان پراکنذگی در چه نقطه ای است؟
plt.text(2, 60, r'Devition of numbers', fontsize=15)
plt.xlabel('values')
plt.ylabel('number of counts')
plt.hist(x, 5) # هیستوگرام با 5 میله
plt.show()

x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 20)
plt.show()

x = numpy.random.normal(5.0, 1.0, 100000)  # اعداد تصادفی با توزیع نرمال تولید کن، یعنی ژراکندگی حول یک مقدار معین متمرکز شوند
plt.hist(x, 100)
plt.show()


