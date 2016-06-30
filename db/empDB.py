###Project 3 
### Martin Murphy
### 05/07/2014
###empDB.py





# Project 3 Option A: complete employ.py and also the 10 methods of this module (empDB.py) that are incomplete.
# Any method that is commented:  "# this is complete" requires no further code, you may use as is.
# selectionSort is provided so you can use it as a model for the extra credit (sorting and searching by any parameter)
# Extra credit (see below): It may be easier to code without the attrib parameter first, searching by last name.

# For empDB.py
# Document each method with a description of what it accomplishes and returns, and how each parameter is used.
# For each method, also state what its big-Oh runtime is and justify your claim
# You may use the following in your runtime justifications:
# The run-time of accessing or modifying an element of a list, or adding an element to the end of a list is constant time
# The run-time of most string operations is linear, except indexing and len, which are constant time.
# The run-time of a slice operation is proportional to the length of the output, but independent of the size of the input.
# For more information on asymptotic run-time analysis, see: 
#  Appendix B Analysis of Algorithms at http://www.greenteapress.com/thinkpython/html/thinkpython022.html 

# Restrictions on use of built-in functions are listed above some of the methods you will code





from employ import *
import copy
 
class empDB:
    def __init__(self, lst= []):                  
      	self.lst = lst

    # Returns string for database output in csv (comma separated values) format: one employee per line, attibutes separated by commas
    def __str__(self):
        prntStr=''
        for i in range(len(self.lst)):
            prntStr+=str(self.lst[i])+'\n'
        return prntStr
        
    # You may use a built-in for the contained list class here
    def __len__(self):
        return len(self.lst)

    # Adds an employee instance onto the end of the list.
    def appendEmp(self, emp=Employee()):						
        self.lst+=[emp]
        return self.lst

    # Do not use slices: code this yourself
    
    def insertEmp(self, index, emp=Employee()):						
        templst=[]
        for i in range(len(self.lst)):
            if i == index:
	        templst+=[emp]
                for j in range(i,len(self.lst)):
        	    templst+=[self.lst[j]]
	        self.lst=templst
		break
	    templst+=[self.lst[i]]
		

# Three standard methods to overload
    # Allows for bracket operator to be used to return indexth element of the empDB
    def __getitem__(self, index):                  
        return self.lst[index]

    # Allows for bracket operator to be used to modify indexth element of the empDB, setting it to val
    
    def __setitem__(self, index, emp=Employee()):  
        self.lst[index] = emp


     # You may use a built-in for the contained list class here
    def __delitem__(self, index):
        templst=[]
        for i in range(len(self.lst)):
            if i == index:
                for j in range(i+1,len(self.lst)):
        	    templst+=[self.lst[j]]
                self.lst=templst
	        break  
	    templst+=[self.lst[i]]


###SEQUENTIAL SEARCH Big-Oh : O(n)  My understanding is that it traverses the list comparing each element in the list to the value passed in.
# Search on the attribute "lastName". For extra credit search on any attribute using: getattr(object, attrib[, defaultAttrib]
    def sequentialSearch(self, val, attrib="lastName"):					
        for i in range(len(self.lst)):
           if val == getattr(self.lst[i], attrib, "lastName"):
                return i
        return -1


###SELECTION SORT Big-Oh : O(n**2) Selection is a Algorithm that finds the smallest attribute and  swaps it to first position in list

# Sorts on any attribute using: getattr(object, attrib[, defaultAttrib])
    def selectionSort(self, attrib="lastName"):      					
        minIndex = 0
        for i in range (len(self.lst)):
            minIndex = i

            for j in range(i+1, len(self.lst)):
                if getattr(self.lst[minIndex], attrib, "lastName") > getattr(self.lst[j],attrib, "lastName"):
                    minIndex = j
 
            temp = self.lst[minIndex]
            self.lst[minIndex] = self.lst[i]
            self.lst[i] = temp

###MERGE SORT Big-Oh : O(n log n)  Separates the unsorted list into lists, each containing 1 element then repeatedly merges 

        # Sort on the attribute "lastName" (ie: sort by last name).
    # For extra credit sort on any attribute using: getattr(object, attrib[, defaultAttrib]).
    def mergeSort(self, attrib= "lastName"):
        self.lst=self.split(self.lst, attrib)

    #divides list into sublists until each element has it's own list and len(lst)=1           
    def split(self,unsortedList, attrib):
        if len(unsortedList)==1:
            return unsortedList[0]
        
	mid = len(unsortedList) / 2
        left = unsortedList[:mid]
        right = unsortedList[mid:]
        
	if len(left)>1:
            left=self.split(left,attrib)
        if len(right)>1:  
            right = self.split(right,attrib)
        
	return self.join(left, right, attrib)
     
    #creates new list from two sublists and moves from smallest sublist to top, 
    
    def join(self,left,right, attrib):
        result=[]
        
	while left and right:
            if getattr(left[0], attrib) < getattr(right[0],attrib):
                result+=[left[0]]
                left=left[1:]
            else:
                result+=[right[0]]
                right = right[1:]
        
	if left:
            result+=left
        else:
            result+=right
        
	return result


 ###INSERTIONSORT Big-Oh : 0(n^2) My understanding of this alg is that a elem  inserted back into the previous sublist where the lower end of list is already sorted                                                                                              
    # Sort on the attribute "lastName" (ie: sort by last name).
    # For extra credit sort on any attribute using: getattr(object, attrib[, defaultAttrib]).
    # def insertionSort(self, attrib="lastName"):

            
    def insertionSort(self, attrib="lastName"):
        index=0
        minx=0
        insx=0
        while insx < len(self.lst):
            while index<len(self.lst):
                if getattr(self.lst[minx], attrib, "lastName") > getattr(self.lst[index], attrib, "lastName"):
                    minx = index
                index +=1
            temp = self.lst[insx]
            self.lst[insx] = self.lst[minx]
            self.lst[minx] = temp
            insx +=1
            index = insx
            minx = insx









###BINARY SEARCH---Big-Oh : O(log n) Performs a recursive binary search function on provided list that is sorted. Takes the list and val and returns i

    # Search on the attribute "lastName" (ie: return index of employee with last name == val).
    # For extra credit search on any attribute using: getattr(object, attrib[, defaultAttrib])
    # Hint: if you code this recursively, then write and call a helper function with parameters lo, hi

    def binSearch(self,val,lo, hi, attrib="lastName"):        
        mid = (hi+lo)/2
        count = 1
        count+=1

        if val == getattr(self.lst[mid], attrib,"lastName"):
            return mid

        elif lo>=hi:
            return -1

        elif val > getattr(self.lst[mid],attrib, "lastName"):
            return self.binSearch(val, mid+1, hi, attrib)

        elif val < getattr(self.lst[mid],attrib, "lastName"):
            return self.binSearch(val, lo, mid-1, attrib)


    def binarySearch(self,val,attrib="lastName"):
        temp=self.mergeSort(attrib)
	lo=0
        hi=(len(self.lst)-1)
        return self.binSearch(val, lo, hi, attrib)




    # Given: listEmpHrsWorked is a list of tuples with (SSID, hrsWorkedThisPeriod) for each employee in the list
    #  Return a new list of tuples for each tuple in listEmpHrsWorked
    # Your new list will contain the following tuple for each SSID in listEmpHrsWorked:
    #  (firstname, lastName, ssID,  hrsWorkedThisPeriod, payThisPeriod)
    def calcPayroll(self, listEmpHrsWorked):
        money = []
        for elem in listEmpHrsWorked:
            index = self.binarySearch(elem[0],"ssID")
            salary = self.lst[index].calc_Salary(elem[1])
            result = [(self.lst[index].firstName,self.lst[index].lastName, elem[0], elem[1],salary)]
            money += result
        return money



        # keep track of two listEmpHrsWorked





## A start on testing: fill in append  and __str__ first:
empList = empDB()
NUM_EMPS = 10
for i in range(NUM_EMPS):
    SSstring =  "696-22-120" + str(i)
    empList.appendEmp(Employee(SSstring, str(NUM_EMPS-i-1), "Employee", date.fromordinal(i*100 + 1), date.today(), 800.00*i ))
    print empList[i]
print
employDB_backup = copy.deepcopy(empList)

## Add more test cases  after you fill in some methods



NUM_EMPS = 5
for i in range(NUM_EMPS):
    SSstring =  "111-22-666" + str(i)
    empList.appendEmp(MaintenanceWorker(SSstring, str(NUM_EMPS-i-1), "Employee", date.fromordinal(i*75 + 1), date.today(), 800.00*i ))




NUM_EMPS = 2
for i in range(NUM_EMPS):
    SSstring =  "333-22-120" + str(i)
    empList.appendEmp(Manager(SSstring, str(NUM_EMPS-i-1), "Employee", date.fromordinal(i*50 + 1), date.today(), 800.00*i ))










 

empList = empDB()
employDB_backup = copy.deepcopy(empList)

empList.appendEmp(AdminAssistant("751-65-2311", "Jobs", "Steve", "2001-02-19", datetime.today(), 20, "Musk","Amazon books" ))
empList.appendEmp(AdminAssistant("451-33-2322", "Bezo", "Jeff", "1980-06-11", datetime.today(), 20, "Musk","Amazon TV "))
empList.appendEmp(Manager("851-75-2338", "Musk", "Elon", "1975-04-14", datetime.today(), 400, ['Scott', 'Washington']))
empList.appendEmp(FactoryWorker("351-43-2348", "Obama", "Barrack", "1988-09-14", datetime.today(), 10, "Yu","Oscorp Bio" ))
empList.appendEmp(FactoryWorker("121-99-2666", "Ferguson", "Neil", "1991-06-24", datetime.today(), 10, "Yu","Oscorp AI"))
empList.appendEmp(Manager("041-79-2348", "Yu", "Toby",  "1993-01-14", datetime.today(), 100, ["Obama","Ferguson"]))
empList.appendEmp(MaintenanceWorker("151-25-9998", "Chavez", "Xavier", "1950-0-11", datetime.today(), 15, "Le","Skyscraper"))
empList.appendEmp(MaintenanceWorker("501-05-2178", "Garibaldi", "Giuseppe", "1986-09-14", datetime.today(), 15, "Le","School"))
empList.appendEmp(Manager("331-15-4448", "Le", "Grace" ,  "2002-04-12", datetime.today(), 100, ["Chavez","Garibaldi"]))


# empList = empDB()
# employDB_backup = copy.deepcopy(empList)

# empList.appendEmp(MaintenanceWorker("111-11-1111", "Chavez", "Xavier", "1995-04-24", date.today(), 25, "Le","StadiumUP"))
# empList.appendEmp(MaintenanceWorker("111-12-1234", "Garibaldi", "Giuseppe", "1995-04-24", date.today(), 25, "Le","StadiumDWN")
# empList.appendEmp(Manager("123-45-6789", "Le", "Grace", "1989-12-03",  date.today(), 1500, ["Chavez","Garibaldi"] )

# empList.appendEmp(AdminAssistant("222-22-2222", "Jobs", "Steve", "1990-06-16", date.today(), 20, "Musk","Amazon ship")
# empList.appendEmp(AdminAssistant("111-12-9999", "Bezo", "Jeff", "1990-06-16", date.today(), 50, "Musk","Amazon receive")
# empList.appendEmp(Manager("123-45-6789", "Musk", "Elon", "1986-06-03",  date.today(), 1000, ["Jobs","Bezo"] )

# empList.appendEmp(FactoryWorker("333-33-3333", "Obama", "Barrack", "2000-04-14", date.today(), 30"Yu","Oscorp Bio")
# empList.appendEmp(FactoryWorker("444-44-4444", "Ferguson", "Neil", "2000-03-14", date.today(), 40, "Yu","Oscorp AI")
# empList.appendEmp(Manager("555-11-6666", "Yu", "Toby", "2000-12-03",  date.today(), 800, ["Obama","Ferguson"] )

#print empList
#Test Cases

print "Unsorted Employee list created by appendEmp functions:"
                                        
print empList

print  '#########################################################################'

print "Insert 'Peter Parker' at index 4 with insertEmp function:"
empList.insertEmp(4,MaintenanceWorker("451-75-2348", "Parker", "Peter", "1983-04-14", datetime.today(), 20, "Le", "Dugout"))
print empList

print "Insert 'Bruce Willis' at index 3 with insertEmp function:"
empList.insertEmp(3,MaintenanceWorker("451-75-2348", "Willis", Buce"", "1960-08-20", datetime.today(), 20, "Le", "Dugout"))
print empList

print '#########################################################################'


print "Selection sort by ssID:"
empList.selectionSort("ssID")
print empList

print '#########################################################################'

print " Insertion Sort list"
empList.insertionSort("lastName")
print empList

print '#########################################################################'

print "Merge sort by firstName:"
empList.mergeSort("firstName")
print empList


print "Merge sort by lastName:"
empList.mergeSort("lastName")
print empList



print  '#########################################################################'

print "Sequntial search for 'Jobs' by lastName"
print empList.sequentialSearch("Jobs","lastName")

print "Sequntial search for 'Ferguson' by lastName"
print empList.sequentialSearch("Ferguson","lastName")


print "Sequntial search for 'Musk' by lastName"
print empList.sequentialSearch("Musk","lastName")

print  '#########################################################################'

print "Binary search for 'Giuseppe' by firstName"
print empList.binarySearch("Giuseppe","firstName")


print "Binary search for 'Peter' by firstName"
print empList.binarySearch("Peter","firstName")


print  '#########################################################################'


print empList.calcPayroll([("501-05-2178",15), ("331-15-4448", 50)])



print  '#########################################################################'



print empList.calcPayroll([("501-05-2178",15), ("331-15-4448", 50), ("751-65-2311",20), ("121-99-2666", 40)])











