RATE = 5.0
INIT_BAL = 10000

numY = 5 #assume user enter 5 years

bal = INIT_BAL

for year in range(1,numY+1):
    interest = bal * RATE/100
    bal = bal + interest
    print(year, bal)


#write an equivalent while loop below:

#let's reinitialize all the variables used above

count = 0 #year
bal = INIT_BAL

while (count < numY):
    interest = bal * RATE/100
    bal = bal + interest
    count = count + 1
    print (count, bal)

    










    
