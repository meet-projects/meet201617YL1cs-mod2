raining = False

have_umbrila = True
if raining and have_umbrila :
    print('get umbrila')
elif raining :
    print('get wet')
else:
    print('have a nice day')


i = 0
'''
while i < 10:
    i += 1
    print(i)
'''
import time



my_list = [1, 2, 3, "monqeth"]
for i in my_list:
    print(i)

for hour in range(12):
    for minute in range(60):
        for second in range(60):
            print(str(hour)+':'+str(minute)+':'+str(second))
            time.sleep(1)
