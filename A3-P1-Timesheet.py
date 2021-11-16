#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     Ashton Burgess
#Student Name:  w0465511
# def timesheet():
#     #initailize the list with a list lenth from 0 to 5
#     timesheet=[]
#     totalHours=0
#     #append work hours per day to the list
#     for i in range(0,5):
        
#         hoursThatDay=int(input("Enter hours worked on day(Integeres Only): "))
#         timesheet.append(hoursThatDay)
#         #totalHours collects and totals all hours
#         totalHours+=hoursThatDay
#     average=totalHours/ 5
#     print("Enter hours worked on Day#{0}: ".format(timesheet))
#     print("The total number of hours worked was{0}. ".format(totalHours))
#     print("The average number of hours worked each day was: {0}".format(average))



def solidLine():
    print("____________________________________________________")

def highestDay(myList):
    print("(The most hours you worked was on: ")
    mostHours=max(myList)
    maxDay=myList.index(mostHours)
    print("The most hours worked was on :\n Day#{0} when you worked {1} hours.".format(maxDay+1, mostHours))




def SlackDays(myList):
    print("Days you slacked off(i.e. worked less than 7 hours): ")
    for i in range(len(myList)):
        if myList[i] < 7:
            print("Day #{0}: {1}".format(i +1, myList[i]))

        
 
def main():
    
    myList=[]
    totalHours=0

    
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