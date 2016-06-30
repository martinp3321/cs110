

###Project 3 
### Martin Murphy
### 04/23/2014
###Employ.py



# classes: without init function defined, an empty object will be instantiated.
#   If init is defined, it will be invoked upon instantiation of an object of the class
# The first parameter of any method/function in the class is always self, the name self is used by convention.
#  The object that the method was called on is passed in for the first parameter, so the function call arguement list has one less arguement than the function definition.


# Project 3 Option A: complete this module (employ.py) and also module empDB.py.
#  __init__ for class EmpHourly is completed for you so you can use it as a model for calling of superclass methods

# For employ.py:
#   Fill in the class definitions where they are incomplete. Code as high up in the hierarchy as possible.
#   Code __init__  and __str__ methods so that each type of employee is correctly instantiated and each attribute coded once only.
#   Code __str__ methods so that each type of employee has all attributes *printed on one line in csv format* (attributes separated by commas only), ** in the order they appear in the __init__ parameter list **.
#   Code calc_salary so that each type of employee has salary calculated correctly. (You may pass hours worked as a parameter.)
#   Call on superclass __init__ and __str__ where appropriate. Call on superclass calc_salary where appropriate.


#from datetime import tzinfo, timedelta, datetime   # http://docs.python.org/library/datetime.html
from datetime import *
import string
import csv



###Employee class creates an object with parameters usually assigned to an employee in a company.  |
###Includes __init__, __str__, and calc_Salary functions.     				 |

	   
class Employee(object):
    
 
### the default attributes of emp being set to Employee()

    def __init__(self, ssID="", lastName="", firstName="",  DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0):
        self.salary = salary
    	self.firstName = firstName 
    	self.lastName = lastName
    	self.ssID = ssID
    	self.DOB = str(DOB)[5:7] + '/' + str(DOB)[8:10] + '/' + str(DOB)[0:4]	 #sliced Datetime to read better
    	self.startDate = str(startDate)[5:7] + '/' + str(startDate)[8:10] + '/' + str(startDate)[0:4]  
    	

    def __str__(self):
	    return self.ssID + "," + self.lastName + "," + self.firstName + "," + str(self.DOB) + "," + str(self.startDate) + "," + str(self.salary)


 


###EmpSalaried class creates a subtype of Employee which has the attributes of Employee 		 |


class EmpSalaried(Employee):
	# salary is for the pay period
    def __init__(self, ssID="", lastName="", firstName="",DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, category="" ):
	super(EmpSalaried, self).__init__(ssID, lastName, firstName, DOB, startDate, salary)

    def __str__(self):
	return super(EmpSalaried, self).__str__()


### hrsWorkedThisPeriod is for uniformity with other Employees and is not used
    def calc_Salary(self, hrsWorkedThisPeriod=0):
	return self.salary

 


###Manager class creates a sub-type of mpSalaried which has the attributes of Employee		 |



class Manager(EmpSalaried):

    def __init__(self, ssID="", lastName="", firstName="", DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, manage=['']):
	super(Manager, self).__init__(ssID, lastName, firstName, DOB, startDate, salary)	#super call to populate basic employee data
	self.manage = manage
	
    def __str__(self):
    	mge = "["
    	if self.manage != []:
    		mge += ";".join(self.manage)
    	mge += "]"


	return super(Manager, self).__str__() + "," + mge  #super call to populate basic employee data for __str__

 


###EmpHourly class creates a sub-type of Employee which has the attributes of Employee 		 |

class EmpHourly(Employee):
    def __init__(self, ssID="", lastName="", firstName="", DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, manager='manager'):
	super(EmpHourly, self).__init__(ssID, lastName, firstName, DOB, startDate, salary)  #super call to populate basic employee data
	self.manager = manager  #adds a manager component to EmpHourly Employee

    def __str__(self):	   #super call to populate basic employee data for __str__ plus self.manager
	return super(EmpHourly, self).__str__() + ',' + str(self.manager)


    def calc_Salary(self, hrsWorkedThisPeriod=0.0):	 #calc_Salary function for all EmpHourly subordinate employee types
	Sal = (hrsWorkedThisPeriod * self.salary)
	#print Sal 
	return " Salary:" + str(Sal)

    #str(Sal)

    #self.lastName

 

###AdminAssistant class creates a sub-type of EmpHourly which has the attributes of EmpHourly	 |

class AdminAssistant(EmpHourly):
    def __init__(self, ssID="", lastName="", firstName="", DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, manager='', department='department'):
	super(AdminAssistant, self).__init__(ssID, lastName, firstName, DOB, startDate, salary, manager)	#super call to populate basic EmpHourly data
	self.department = department

    def __str__(self):
	return super(AdminAssistant, self).__str__() + " " + str(self.department)


    def calc_Salary(self, hrsWorkedThisPeriod = 0.0):
	return super(AdminAssistant, self).calc_Salary(hrsWorkedThisPeriod)

 



###FactoryWorker class creates a sub-type of EmpHourly which has the attributes of EmpHourly

###+ the inclusion of a assemblyLine parameter assigned to each FactoryWorker . 


class FactoryWorker(EmpHourly):
    def __init__(self, ssID="", lastName="", firstName="", DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, manager='', assemblyLine='assemblyLine'):
	super(FactoryWorker, self).__init__(ssID, lastName, firstName, DOB, startDate, salary, manager)	 #super call to populate basic EmpHourly data
	self.assemblyLine = assemblyLine


    def __str__(self):
	return super(FactoryWorker, self).__str__() + "," + str(self.assemblyLine)


    def calc_Salary(self, hrsWorkedThisPeriod = 0.0):
	return super(FactoryWorker, self).calc_Salary(hrsWorkedThisPeriod)




### MaintenanceWorker class creates a sub type of EmpHourly which has the attributes of EmpHourly

class MaintenanceWorker(EmpHourly):

    def __init__(self, ssID="", lastName="", firstName="", DOB=datetime.fromordinal(1), startDate=date.today(), salary=0.0, manager='', buildings=[]):
	super(MaintenanceWorker, self).__init__(ssID, lastName, firstName, DOB, startDate, salary, manager)
 ###super call to populate basic EmpHourly data
	
	self.buildings = str(buildings)


    def __str__(self):
	return super(MaintenanceWorker, self).__str__() + "," + str(self.buildings)


    def calc_Salary(self, hrsWorkedThisPeriod = 0.0):
	return super(MaintenanceWorker, self).calc_Salary(hrsWorkedThisPeriod)





emp1 = Employee("111-11-1111", "Chavez", "Xavier", "1995-04-24", date.today(), 40)
emp2 = MaintenanceWorker("111-12-1234", "Garibaldi", "Giuseppe", "1995-04-24", date.today(), 45, "Le","Church")
emp3 = Manager("123-45-6789", "Le", "Grace", "1989-12-03",  date.today(), 80, ["Chavez","Garibaldi"] )

emp4 = Employee("222-22-2222", "Jobs", "Steve", "1990-06-16", date.today(), 50)
emp5 = AdminAssistant("111-12-9999", "Bezo", "Jeff", "1990-06-16", date.today(), 50, "Musk","Amazon")
emp6 = Manager("123-45-6789", "Musk", "Elon", "1986-06-03",  date.today(), 1000, ["Jobs","Bezo"] )

emp7 = Employee("333-33-3333", "Obama", "Barrack", "2000-04-14", date.today(), 60)
emp8 = FactoryWorker("444-44-4444", "Ferguson", "Neil", "2000-03-14", date.today(), 50, "Yu","China")
emp9 = Manager("555-11-6666", "Yu", "Toby", "2000-12-03",  date.today(), 100, ["Obama","Ferguson"] )

print emp1
print emp2
print emp3

print emp4
print emp5
print emp6

print emp7
print emp8
print emp9

print emp2.calc_Salary(1)


print emp5.calc_Salary(2)


print emp8.calc_Salary(3)

print emp9.calc_Salary(3)








##prints out as:
##111-11-1111,Chavez,Xavier,1995-04-24,2014-04-18,25
##111-12-1234,Garibaldi,Giuseppe,1995-04-24,2014-04-18,25,Le,[]
##123-45-6789,Le,Grace,1989-12-03,2014-04-18,1500,Manager,[Chavez;Garibaldi]

#test all functionality, including calc_Salary, for an object of each class



