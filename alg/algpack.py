##Project 2 
##CS110 2014 Spring
##Martin Murphy
##ALGORITHM PACK
##String and List Algorithms without built in modules from python








def repeatList(lst, n):
	"""
	>>> repeatList([1,2,3], 0)
	[]
	>>> repeatList([1,2,3], 1)
	[1, 2, 3]
	>>> repeatList([1,2,3], 2)
	[1, 2, 3, 1, 2, 3]
	>>> repeatList([1,2,3], 3)
	[1, 2, 3, 1, 2, 3, 1, 2, 3]
	>>> repeatList([1,2,3], 5)
	[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
	>>> repeatList([0,0,0], 1)
	[0, 0, 0]
	>>> repeatList([33,11,666], 06)
	[33, 11, 666, 33, 11, 666, 33, 11, 666, 33, 11, 666, 33, 11, 666, 33, 11, 666]
	>>> repeatList([1,2,3], 10)
	[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
	>>> repeatList([a], 0)
	[]
	>>> repeatList([1], 1)
	[1]
	>>> repeatList([100], 3)
	[100, 100, 100]
	>>> repeatList([1], 10)
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	"""

	answer=[]
	
	if n ==0:
		lst = answer
	
	while n > 0:
		answer += lst 
		n -= 1 
	
	return answer



def replace(lst, pos, item):
	"""
	Modifies list lst so that its element at pos is replaced with item.
	Does not modify lst if pos is negative or pos >= length of lst.
	Nothing is returned.
	Examples:
	>>> list = [1,2,3]
	>>> replace(list,2,'z')
	[1, 2, 'z']
	>>> list = [1,3,4]
	>>> replace(list,1,'z')
	[1, 'z', 4]
	>>> list = [1]
	>>> replace(list,0,'z')
	['z']
	>>> list = [1,2,3]
	>>> replace(list,1,'z909')
	[1, 'z909', 3]
	"""
	answer = []
	

	if pos<0 or pos>=len(lst):
		return lst
	

	else:
		 lst[pos] = item
	

	for elem in lst:
			answer +=[elem]
	
	return answer





def countElem(lst, elem):
	"""
	Returns the number of occurrences of element elem in list lst
	Examples:
	>>> countElem(['w', 'owl', 'w', 'awesome'], 'w')
	2
	>>> countElem(['w', 'abc', 'w', 'abc'], 'w')
	2
	>>> countElem(['b', 'b', 'b', 'awesome'], 'b')
	3
	>>> countElem(['w', 'owl', 'w', 'awesome'], 'z')
	0
	>>> countElem(['w', '0', 'w', '0'], '0')
	2
	>>> countElem(['www', 'ww', 'w', 'w'], 'w')
	2
	>>> countElem(['hello', 'world', 'w', 'awesome'], 'world')
	1
	>>> countElem(['1'], '1')
	1
	>>> countElem(['2', '2', '2', '2'], 'w')
	0
	>>> countElem([], '')
	0
	"""
	count = 0 
	

	for char in lst:
		
		if char == elem:
			count +=1
	
	return count








def findLast(lst, elem):
	"""
	Returns the index of the last occurrence of element elem in list lst or -1 if elem does not
	occur in lst.
	Examples:
	>>> findLast(['w', 'owl', 'w', 'awesome'], 'w')
	2
	>>> findLast(['a', 'ya', 'a', 'yahoo'], 'a')
	2
	>>> findLast(['w', 'owl', 'w', 'awesome', 'w'], 'w')
	4
	>>> findLast(['w', 'owl', 'e', 'awesome'], 'w')
	0
	>>> findLast(['w', 'owl', 'w', 'awesome', '1', '2'], '2')
	5
	>>> findLast(['w', 'owl', 'w', 'woody'], 'woody')
	3
	>>> findLast(['woody', 'owl', 'w', 'woody'], 'w')
	2
	>>> findLast(['w', 'w', 'w', 'w'], 'w')
	3
	>>> findLast(['0', '1', '2', '3'], '1')
	1
	>>> findLast(['0', '1', '2', '3'], '')
	-1
	"""
	for i in range(len(lst)-1, -1 , -1):
		
		if lst[i] == elem:
			
			return i 
	
	return -1










def string2list(s):
	"""
	Returns a list whose elements are each of the characters in string s as ordered in s
	Examples:
	>>> string2list ('cat')
	['c', 'a', 't']
	>>> string2list ('dog')
	['d', 'o', 'g']
	>>> string2list ('yahoo')
	['y', 'a', 'h', 'o', 'o']
	>>> string2list ('')
	[]
	>>> string2list ('a')
	['a']
	>>> string2list ('1234')
	['1', '2', '3', '4']
	>>> string2list ('computer')
	['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']
	>>> string2list ('new')
	['n', 'e', 'w']
	>>> string2list ('000')
	['0', '0', '0']
	>>> string2list ('game')
	['g', 'a', 'm', 'e']
	>>> string2list ('abcde')
	['a', 'b', 'c', 'd', 'e']
	"""

	lst = []
	
	for char in s:
		
		lst+= [char]
	
	return lst









def numOccur(lst, char):
	count = 0 
	
	for elem in lst:
		
		if elem == char:
			count += 1 

	
	return count 



def lastOccurMostFreqElem(lst):
	"""
	Returns the index of the last occurrence of the element that most frequently occurs
	in list lst or -1 if lst is empty.
	Examples:
	>>> lastOccurMostFreqElem([0,0,2,2,0,2])
	5
	>>> lastOccurMostFreqElem([0,0,2,0,2])
	3
	>>> lastOccurMostFreqElem([0])
	0
	>>> lastOccurMostFreqElem([0,0,2,2,9,9,9,9,0,2])
	7
	>>> lastOccurMostFreqElem([])
	-1
	>>> lastOccurMostFreqElem([0,0,0,0,0,0,0,0,0,0])
	9
	"""

	nummf = 0 
	
	elemmf = -1
	

	for elem in range(len(lst)):
		
		count = numOccur(lst, lst[elem])
		
		if count >= nummf:
			nummf = count
			elemmf = elem
	

	return elemmf









def insert(s1, s2, pos): 
 """ 
 Returns a new string that is equivalent to string s1 with string s2 inserted at index pos. 
 Returns empty string if pos is negative or pos > length of s1. 
 Examples: 
 >>> insert('i', 'world!', 0) 
 'world!i'
 >>> insert('see', 's', 3) 
 'sees'
 >>> insert('yea', 'you', 2)
 'yeyoua'
 >>> insert('', '', 0) 
 ''
 >>> insert('e', 'woo', 0) 
 'wooe'
 >>> insert('spaces', 's', 5) 
 'spacess'
 

 """ 
 
 if pos<0 or pos>len(s1):
     return ''

     

 nl=""
 for i in range(len(s1)):

     
     
     if i==pos:
    
         nl+=s2
         nl+=s1[i]
         return nl
             
     nl+=s1[i]

 if pos==len(s1):
     nl+=s2
     
 
 
 

 return nl







def substring (s, pos1, pos2):
	"""
	>>> substring('cat',0,3)
	'cat'
	>>> substring('denver',0,3)
	'den'
	>>> substring('denver',3,6)
	'ver'
	>>> substring('abcdefghi',4,9)
	'efghi'
	"""

	answer = ''
	lst = []
	if pos2 > len(s) or pos1 > pos2:
		return ""

	for char in s:
		lst += char
	for pos, elem in enumerate(lst):
		for num in range(pos1, pos2):
			if pos == num:
				answer += elem
	return answer







def str2int(s):
	"""
	>>> str2int('246')
	246
	>>> str2int('12345')
	12345
	>>> str2int('33')
	33
	>>> str2int('11')
	11
	>>> str2int('-11')
	-11
	>>> str2int('0')
	0
	>>> str2int('6')
	6
	>>> str2int('666666')
	666666
	>>> str2int('22')
	22
	>>> str2int('-0')
	0
	>>> str2int('')
	''
	"""
	if s[0] == '-':
			strt=1

	else:
		strt =0

	answer=0


	for i in range (strt,len(s)):



		intchar= ord(s[i])

		intchar= intchar-48



		answer= (answer * 10) + intchar

	if strt ==1:
		answer=  answer * -1




	return answer







def int2str(i):
	"""
	Returns a string that is the string equivalent of valid integer i
	Examples:
	>>> int2str(-1000092)
	'-1000092'
	>>> int2str(-10)
	'-10'
	>>> int2str(1000092)
	'1000092'
	>>> int2str(33)
	'33'
	>>> int2str(11)
	'11'
	>>> int2str(-33)
	'-33'
	>>> int2str(666)
	'666'
	>>> int2str(-10000920)
	'-10000920'
	>>> int2str(0)
	''
	>>> int2str(311666)
	'311666'
	"""

	neg=False

	answer=""

	if i<0:
	    
	    i=i*(-1)
	    
	    neg=True

	while i>0:
	    
	    left=i%10
	    
	    i=i/10
	    
	    str1= chr(left+48)
	    
	    answer=str1 + answer

	if neg:
	    answer= "-" + answer
    
    
	return answer






def sortList(mylist):

	"""
	Modifies list lst so that it is sorted in ascending order using the selection sort algorithm.
	Nothing is returned.
	Assumes the elements of lst are comparable.
	Examples:
	>>> mylist = [1, 5, 9, 2, 0, 8]
	>>> sortList(mylist)
	>>> mylist
	[0, 1, 2, 5, 8, 9]
	>>> mylist = [1, 5, 9, 2, 0, 8, 0, 0]
	>>> sortList(mylist)
	>>> mylist
	[0, 0, 0, 1, 2, 5, 8, 9]
	>>> mylist = [1, 5, 9, 2, 0, 8, 9, 9]
	>>> sortList(mylist)
	>>> mylist
	[0, 1, 2, 5, 8, 9, 9, 9]
	>>> mylist = [1, 5]
	>>> sortList(mylist)
	>>> mylist
	[1, 5]
	>>> mylist = [0,0,0,0,1]
	>>> sortList(mylist)
	>>> mylist
	[0, 0, 0, 0, 1]
	>>> mylist = [9,8,7,6,5,4,3,2,1]
	>>> sortList(mylist)
	>>> mylist
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> mylist = [0]
	>>> sortList(mylist)
	>>> mylist
	[0]
	>>> mylist = [1]
	>>> sortList(mylist)
	>>> mylist
	[1]
	>>> mylist = [100]
	>>> sortList(mylist)
	>>> mylist
	[100]
	>>> mylist = [1,99,0]
	>>> sortList(mylist)
	>>> mylist
	[0, 1, 99]
	>>> mylist = [100,99]
	>>> sortList(mylist)
	>>> mylist
	[99, 100]
	"""
	
	for s in range(len(mylist)-1,0,-1):
         Mx=0
         for loc in range(1,s+1):
             if mylist[loc]>mylist[Mx]:
                 Mx = loc

         zy = mylist[s]
         mylist[s] = mylist[Mx]
         mylist[Mx] = zy





def sortList2(mylist):
	"""
	# Let N be the number of elements in lst and k be the number of buckets.
	# Your algorithm must have runtime O(k+N) , not kN
	def sortList2(lst):

	# Returns a new list containing all the elements of lst sorted in ascending order,
	# employing a specialized bucket sort with one bucket for each integer.
	# Assumes all the elements of lst are integers between 1 and 100 inclusive.
	# Examples:
	>>> sortList2([1, 5, 9, 2, 0, 8])
	[0, 1, 2, 5, 8, 9]
	>>> sortList2([8, 1, 57, 39, 72, 57, 39, 8, 1])
	[1, 1, 8, 8, 39, 39, 57, 57, 72]
	>>> sortList2([9, 8, 7, 6, 5, 4, 3, 2, 1])
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> sortList2([6, 1])
	[1, 6]
	>>> sortList2([8, 1, 57, 39, 72, 57, 39, 8, 1,89,100])
	[1, 1, 8, 8, 39, 39, 57, 57, 72, 89, 100]
	>>> sortList2([0,0,0,3,2,100])
	[0, 0, 0, 2, 3, 100]
	>>> sortList2([3,2,1,1])
	[1, 1, 2, 3]
	>>> sortList2([2,2,2,2,99])
	[2, 2, 2, 2, 99]
	>>> sortList2([1,0,1,0,1])
	[0, 0, 1, 1, 1]
	>>> sortList2([33,3,11])
	[3, 11, 33]
	>>> sortList2([100,100])
	[100, 100]
	>>> sortList2([0,0001])
	[0, 1]
	"""



	head=[0]*101
	answer=[]

	for i in range(len(mylist)):
	
		head[mylist[i]]+=1

	




	for i in range(len(head)):
	
		answer+=head[i]*[i]
	
	return answer      







if __name__ == '__main__':
	import doctest
	doctest.testmod()
