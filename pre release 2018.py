CowID=[] 
CountDays=0
CountCows=int(0)
Yield1=0.0
Yield2=0.0
DailyYield=0
WeeklyYieldArray=[]
DailyYieldArray=[]
LessYield=0
LessYieldArray=[]
WeeklyVol=0
WeeklyCowVol=0
HighestAverage=[]
TempWeek=0
HighestYield=0
#variables and constants declared

def UniqueID():
    CowEntry=int(input("Please enter Cow ID: "))
    if CowEntry not in CowID and (CowEntry>99 and CowEntry<1000):
        CowID.append(CowEntry) #Move CowEntry to CowID
    else:
        print("Cow ID must be unique and 3 digits")
        print("Please enter again")
        UniqueID()
        
#UniqueID function is created 
HerdSize=int(input("Please enter the Size of the Herd: ")) #To ensure the herd size is fixed
for CountCows in range (HerdSize): #determining how many iteration of the loop base on the variable herdsize
    UniqueID() #It calls the UniqueID function to input Cow ID (CowEntry variable)

    for CountDays in range(1,8): #determining how many interation of a range(7)
        print("Day", CountDays)#Output CountDays, increases by 1 in every iteration
        print("Please enter the first Yield for Cow", CowID[CountCows]) 
        Yield1=float(input())
        print("Please enter the Second Yield for Cow", CowID[CountCows])
        Yield2=float(input())#The system will ask user ro enter both yields
        DailyYield=Yield1+Yield2# TASK 2 START - Adds the value binded by Yield1 & Yield2 together
        DailyYieldArray.append(DailyYield)#Adding the value bound DailyYield to the DailyYieldArray
        WeeklyVol=WeeklyVol+DailyYield#Adding the DailyYield to WeeklyVol for each day for each cow
        TempWeek+=DailyYield #Adding DailyYield to 1 to TempWeek for each day for each cow
        AveragePerCow=WeeklyVol/7# dividing the WeeklyVol by 7 to find the average yield per cow
        TempAverage=TempWeek/7 # dividing the TempWeek by 7 to find the TempAverage 

        if DailyYield<12: #Ask if the DailyYield is less than 12L
            LessYield+=1  # Adding 1 to the variable LessYield if identifies the DailyYield which produced less than 12L

    LessYieldArray.append(LessYield) #Append LessYield to LessYieldArray
    WeeklyYieldArray.append(TempWeek)#Append TempWeek to the array WeeklyYieldArray
    LessYield=0 # setting up the LessYield back to '0' for the next cow 


    HighestAverage.append(round(TempAverage))  # Rounding TempAverage yield as told from the task while appending it to HighestAverage
    TempAverage=0#TempAverage return to 0 for the next cow
    TempWeek=0#Temporary yield of the week return to 0 for the next cow

print("Thank You") #printing thank you
print('\n') #space between lines
print("Weekly Volume of milk for the herd is: ", round(WeeklyVol))#printing weekly volume
print('\n') #space between lines
for j in range (HerdSize):  #determining how many iteration of a range (HeardSize)
    print("The average volume of litres for Cow", CowID[j], "is: ",HighestAverage[j]) #print cow with highest average through using the maximum value
    HighestYield=max(WeeklyYieldArray)  # finding which cow produced the HighestYield from the maximum value of WeeklyYieldArray
print('\n') #space between lines - END OF TASK 2

for j in range (HerdSize):  #determining how many iteration of a range (HeardSize)
    if LessYieldArray[j]>=4: #finding which cow produced less than 12L for 4 or more days 
        print("Cow ",CowID[j], "produced less than 12 litres on", LessYieldArray[j], "day(s)") #print the cows that produced less than 12 litres in the LessYieldArray
        print('\n') #space between lines

print("Most productive cow(s) of the week with the highest value:")  #printing
for j in range (HerdSize):  #determining how many iteration of a range (HeardSize)
    if WeeklyYieldArray[j]==HighestYield: # cow which produced the most milk in a week
        print("Cow",CowID[j],"which produced",round(HighestYield),"litres")  #printing the CowID which produced the HighestYield and that yield rounded
print('\n') #Space between a line
programexit=input("Hit Enter to close the program") #Hit enter to exit 
             
