counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
for i in range(1,1338):
    if i % 7 == 0:
        counter1 +=1
        print "i = %i og counter1 = %i" %(int(i),counter1)
        if (counter1 % 7 == 0) or '7' in str(counter1):
            counter2 += 1
            print "i = %i og counter2 = %i" %(int(i),counter2)
            if (counter2 % 7 == 0) or (counter2 % 10 == 7):
                counter3 += 1
                print "i = %i og counter3 = %i" %(i,counter3)
                if (counter3 % 7 == 0) or (counter3 % 10 == 7):
                    counter4 += 1
                    print "i = %i og counter4 = %i" %(i,counter4)
    else:
         if '7' in str(i):
             counter1 += 1
             print "i = %i og counter1 = %i" %(int(i),counter1)
             if (counter1 % 7 == 0) or '7' in str(counter1):
                 counter2 += 1
                 print "i = %i og counter2 = %i" %(int(i),counter2)
                 if (counter2 % 7 == 0) or (counter2 % 10 == 7):
                     counter3 += 1
                     print "i = %i og counter3 = %i" %(i,counter3)
                     if (counter3 % 7 == 0) or (counter3 % 10 == 7):
                         counter4 += 1
                         print "i = %i og counter4 = %i" %(i,counter4)

## Genial losning som ikke er min
#import numpy as np
#numbers = np.arange(1, 1338)
#index = 0
#for num in numbers:
#    if num%7 == 0 or '7' in str(num):
#        numbers[num-1] = numbers[index]
#        index += 1
#print numbers[1336]
