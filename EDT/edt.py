
from logging import NullHandler


class Employee:
    def __init__(self, first_name : str, last_name : str, disponibilites : list, rank : str, contractType : str):
        self.first_name = first_name
        self.last_name = last_name
        self.finalSchedule = []
        self.disponibilites = disponibilites
        self.rank = rank                            #rank = poste
        self.nbrworkinghours = 0
        self.contractType = contractType            #CDI/CDD/BRIGAD/EXTRA ...

    def scheduleChange(self, times : list):
        self.finalSchedule = times
        #print("Horaires de %s changés avec succès" % (self.first_name + " " + self.last_name))

    def disponibilitesChange(self, times : list):
        self.disponibilites = times

    def assignNbrWorkingHours(self, hours : float):
        self.nbrworkinghours = hours




#classe emploi du temps

class EDT():
    def __init__(self, name : str):
        self.name = name
        self.week = None

    def createWeek(self, services : list):
        self.week = services


    



class Service():
    def __init__(self, name : str, times : list, nEmployees : list):        #nEmployees = nombre d'employés nécessaires à chaque poste
        self.name = name
        self.times = times          
        self.nManager = nEmployees[0]
        self.nChefDeRang = nEmployees[1]
        self.nBarman = nEmployees[2]
        self.nOfficier = nEmployees[3]

    def changeSchedule(employees, times):
        for employee in employees :
            pass





times = [[["9:00", "15:00"]],                       #manager
        [["9:00", "15:00"], ["11:00", "16:00"]],    #chefs de rang
        [["9:00", "15:00"]],                        #bar
        [["9:00", "15:00"]]]                        #office

        


def timeToFloat(time : str):
    middle = 0
    for i in range(len(time)):
        if time[i] == ":":
            middle = i
    
    hours = float(time[0:middle])
    minutes = float(time[middle+1:])

    return(hours + minutes/60)


def floatToTime(time : str):

    hours = int(time//1)
    minutes = int(60*(time%1))

    return("%i" % hours + ":" + "%i" % minutes)



print(floatToTime(timeToFloat("15:30")))




quentin = Employee("Quentin", "Bernhard", [], "officier", "extra")
quentin.scheduleChange([1])
    
