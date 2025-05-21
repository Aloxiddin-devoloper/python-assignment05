pul=38500
a_10=pul//10000 #3ta 10minglik
a_5=(pul%10000)//5000 # 1ta 5minglik
a_2=((pul%10000)%5000)//2000 #1ta 2minglik
a_500=(((pul%10000)%5000)%2000)//500 #3ta 500so'mlik
print(a_10, "ta 10000 so'mlik", a_5, "ta 5000 so'mlik", a_2,"ta 2000 so'mlik", a_500, "ta 500 so'mlik")
