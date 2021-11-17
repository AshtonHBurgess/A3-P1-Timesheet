#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     Ashton Burgess
#Student Name:  w0465511

#Program Will take amount of hours worked, and give back total, average, slack days and highest worked day
#need a list for hours and position will be day
#We know the work week is 5 days long

def solidLine():
    print("____________________________________________________")

#get max day
def highestDay(myList):
    print("(The most hours you worked was on: ")
    mostHours=max(myList)
    maxDay=myList.index(mostHours)
    print("The most hours worked was on :\n Day #{0} when you worked {1} hours.".format(maxDay+1, mostHours))



#get slack days
def SlackDays(myList):
    print("Days you slacked off(i.e. worked less than 7 hours): ")
    for i in range(len(myList)):
        if myList[i] < 7:
            print("Day #{0}: {1}".format(i +1, myList[i]))

        
 
def main():
    
    myList=[]
    totalHours=0

    #make list and append hours to the day position
    for count in range(0,5):
        hours=int(input("Enter hours worked on Day #{0}: ".format(count+1)))
        myList.append(hours)
        totalHours= totalHours + hours
  
    average= totalHours/5
    
    solidLine()

    highestDay(myList)

    solidLine()

    print("the total hours worked was: {0}".format(totalHours))
    print("The average hours worked was: {0}".format(average))
    
    solidLine()

    SlackDays(myList)
   
main()