import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]   # سن ماشبن
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]   # سرعت ماشین

# رگرسیون خطی برای پیدا کردن رابطه بین متغیرها استفاده میشود
slope, intercept, r, p, std_err = stats.linregress(x, y)  # متد رگرسیون ، مقادیر کلیدی مهمی را برمیگرداند

# r, be manaye zarib hambastegi hastesh, meghdar r bin -1 ta +1 hastesh, agar r=0 bood yani bin do motaghayer rabteh vojod nadarad,
# v agar r =1 ya -1 bood, anga %100 rabteh vojod darad.

# r= -.76
# وجه: نتیجه 0.76- نشان می دهد که یک رابطه وجود دارد، نه کامل، اما نشان می دهد که می توانیم از رگرسیون خطی در پیش بینی های آینده استفاده کنیمت
print("r =" , r)


def myfunc(x):  # تابع مدلسازی رگرسیون خطی
  return slope * x + intercept   #  این تابع، در محور ایگرگها، مقدار متناظر در محور ایکسها را بدست اورده و برمیگرداند

mymodel = list(map(myfunc, x))  #   با فراخوانی تابع، لیستی آرایه ای جهت مدلسازی بدست می اید

plt.scatter(x, y)      # نمودار پراکندگی نقاط ایکس و ایگرگ را ترسیم میکند
plt.plot(x, mymodel)  # این هم رگرسیون خطی را ترسیم میکند
# با توجه به شیب خط رگرسیون، متوجه میشیم که هر ژقدر سن ماشین بالاتر میره، آنگاه سرعت هم ژایینتر میاذ
plt.show()

# حالا میخواهیم سرعت ماشین ده ساله رو ، پیش بینی کنیم

speed = myfunc(10)

print(speed)
x.append(10)  # 10 ro be end x array add kardam
y.append(speed) # speed be end y array add kardam
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("New r =" , r)
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


