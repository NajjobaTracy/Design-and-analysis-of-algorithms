#Cafeteria Management Tool
#Mark meal cards.
class student:
    def __init__(self,name,regno,accessno,course,hasEaten):
        self.name=name
        self.regno=regno
        self.accessno=accessno
        self.course=course
        self.hasEaten=hasEaten
        self.day=day
        self.studentList=studentList
class servingRota:
    def __init__(self,dayOfWeek,studentList):
        self.dayOfWeek=dayOfWeek
        self.studentList=studentList

dailyRota=[]

studentMealList=[]

studentMealList.append(student("Q","S21B23/019","A94172","B23","THURSDAY","FALSE"
))
studentMealList.append(student("A","S21B13/060","A94446","B13","THURSDAY","TRUE"))

dailyRota.append(servingRota("Monday",studentMealsList))
dailyRota.append(servingRota("Tuesday",studentMealsList))
dailyRota.append(servingRota("Wednesday",studentMealsList))

     


#The algorithm searches through a nested list
#When the student is found, the algorithm finds out if the student has not eaten
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day == dayOfTheWeek):
            for student in day.studentList:
                if(registrationNumber == student.registrationNumber):
                    if(not student.hasEaten):
                        return True

    return False

#Write a function that will update the Cafeteria's registry to "hasEaten" attribute to True, when
print()