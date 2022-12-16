#Cafeteria Management Tool

# time complexity of O(n)
from calendar import day_abbr


class Student:
    def __init__ (self,name,registrationNumber,accessNumber,course,dayofweek,hasEaten):#add day of week attribute to student class
        self.name = name
        self.registrationNumber = registrationNumber
        self.accessNumber = accessNumber
        self.course = course
        self.hasEaten = hasEaten
        self.dayofweek=dayofweek
        





#When the student is found, the algorithm finds out if the student has not eaten
 
def linearsearch(StudentMealsList,registration_Number,days) :
    for day in StudentMealsList:
        
        if day.dayofweek==days and day.registrationNumber==registration_Number:#Check for both the day of week and registration number 
            
                if (day.hasEaten==True ):
                    return "Student has eaten,SHOULDNOT get food"# If the student has eaten ,he shouldnt eat again on that day
                return "Student can go and eat"#He hasnt eaten he can go eat 
        if day.dayofweek!=days and  day.registrationNumber==registration_Number:
            return "Incorrect day"
        if day.dayofweek==days and day.registrationNumber!=registration_Number :
            return "Incorrect Registration Number"
        if day.dayofweek!=days and day.registrationNumber!=registration_Number :
            return "Incorrect Registration Number and day"
                    
StudentMealsList=[]

StudentMealsList.append(Student("Q","S21B23/019", "A94172","B23","THURSDAY",False))#Using test values 
StudentMealsList.append(Student("S","S21B23/023", "A93581","B13","THURSDAY",True))
StudentMealsList.append(Student("A","S21B23/060", "A94446","B13","THURSDAY",True))


print(linearsearch(StudentMealsList,"S21B23/019","THURSDAY"))