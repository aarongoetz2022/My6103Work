###############  HW  Functions      HW  Functions         HW  Functions       ###############
#%%
# ######  QUESTION 1   First, review Looping    ##########
# Write python codes to print out the four academic years for a typical undergrad will spend here at GW. 
# Starts with Sept 2021, ending with May 2025 (total of 45 months), with printout like this:
# Sept 2021
# Oct 2021
# Nov 2021
# ...
# ...
# Apr 2025
# May 2025
# This might be helpful:
# If you consider Sept 2021 as a number 2021 + 8/12, you can continue to loop the increament easily 
# and get the desired year and month. (If the system messes up a month or two because of rounding, 
# that's okay for this exercise).
# And use this (copy and paste) 
# monthofyear = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')
# to simplify your codes.


monthofyeartuple = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')

import datetime


year = 2021
month = 8
my_date = datetime.date(year, month, 8)
delta = datetime.timedelta(months=45)
months = []

while my_date.month == month:
    months.append((my_date).strftime('%d-%b-%Y'))
    my_date += delta

print(months)
print(len(months))





    

###############  Now:     Functions          Functions             Functions       ###############
# We will now continue to complete the grade record that we were working on in class.

#%%
###################################### Question 2 ###############################
# let us write a function find_grade(total) 
# which will take your course total (0-100), and output the letter grade (see your syllabus)
# have a habbit of putting in the docstring
total = 62.1

def find_grade(total):
  '''
  Converting total points into letter grade 
  :param float total: any value between 0 - 100
  :return: str
  '''
  result = 'A' if total >= 93 else 'A-' if total >= 90 else 'B+' if total >= 87 else 'B' if total >= 83 else 'B-' if total >= 80 else 'C+' if total >= 77 else 'C' if total >= 73 else 'C-' if total >= 70 else 'D'
  return result


# Try:
print(find_grade(total))

# Also answer these: 
# What is the input (function argument) data type for total? float
# What is the output (function return) data type for find_grade(total) ? string


#%%
###################################### Question 3 ###############################
# next the function to_gradepoint(grade)
# which convert a letter grade to a grade point. A is 4.0, A- is 3.7, etc
grade = 'C-'

def to_gradepoint(grade):
  # write an appropriate and helpful docstring
  # ??????    fill in your codes here, be sure you have all A, A-, ... thru D, and F grades completed.
  # gradepoint = ???
  '''
  Converting letter grade into grade point 
  :param str: any letter grade between A - F
  :return: float
  '''
  result = 4.0 if grade >= 'A' else 3.7 if grade >= 'A-' else 3.3 if grade >= 'B+' else 3.0 if grade >= 'B' else 2.7 if grade >= 'B-' else 2.3 if grade >= 'C+' else 2.0 if grade >= 'C' else 1.7 if grade >= C- else 1.3 if grade >= D+ else 1.0 if grade >= D else .7 if grade >= 'D-' else 0 if grade >= 'F'
  return result

# Try:
print(to_gradepoint(grade))

# What is the input (function argument) data type for find_grade? string
# What is the output (function return) data type for find_grade(grade) ? float


#%%
###################################### Question 4 ###############################
# next the function to_gradepoint_credit(course)
# which calculates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def to_gradepoint_credit(course):
  # write an appropriate and helpful docstring
  '''
  Converting grade point into grade point credit
  :param float: 0-4 gpa scale
  :return: float
  '''
  result = 12.0 if course 4.0 else 11.1 if course 3.7 else 9.99 if course 3.3 else 9 if course 3.0 else 8.1 if course 2.7 else 6.9 if course 2.3 else 6 if course 2.0 else 5.1 if course 1.7 else 3.9 if course 1.3 else 3.0 if course 1.0 else 2.1 if course .7 else 0 if course 0
  return result
  # ??????    fill in your codes here
  # grade_point_credit = ?????
  # eventually, if you need to print out the value to 2 decimal, you can 
  # try something like this for floating point values %f
  # print(" %.2f " % grade_point_credit)
  return grade_point_credit

# Try:
print(" %.2f " % to_gradepoint_credit(course) )

# What is the input (function argument) data type for to_gradepoint_credit? float
# What is the output (function return) data type for to_gradepoint_credit(course) ? float


#%%
###################################### Question 5 ###############################
# next the function gpa(courses) to calculate the GPA 
# It is acceptable syntax for list, dictionary, JSON and the likes to be spread over multiple lines.
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2020, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2020, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2020, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2020, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2021, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2021, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2021, "grade":'A-', "credits":3 } 
  ]

def find_gpa(courses):
  # write an appropriate and helpful docstring
  '''
  Converting grade point credit into gpa
  :param float: 0-12 gpa credit scale
  :return: float
  '''
  total_grade_point_credit =0 # initialize 
  total_credits =0 # initialize
  # ??????    fill in your codes here
  result = 4.0 if courses 12.0 else 11.1 if courses 3.7 else 9.99 if courses 3.3 else 9 if courses 3.0 else 8.1 if courses 2.7 else 6.9 if courses 2.3 else 6 if courses 2.0 else 5.1 if courses 1.7 else 3.9 if courses 1.3 else 3.0 if courses 1.0 else 2.1 if courses .7 else 0 if courses 0
  return result
  return result
  # gpa = ?????
  return gpa

# Try:
print(" %.2f " % find_gpa(courses) )

# What is the input (function argument) data type for find_gpa? float
# What is the output (function return) data type for find_gpa(courses) ? float


#%%
###################################### Question 6 ###############################
# Write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, it will display the print.
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def printCourseRecord(course):
  # write an appropriate and helpful docstring
  '''
  Print single classs grade
  :param float: single class grade
  :return: none
  '''
  # use a single print() statement to print out a line of info as shown here
  # 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
  # ??????    fill in your codes here
  return # or return None
  
# Try:
printCourseRecord(course)

# What is the input (function argument) data type for printCourseRecord? float
# What is the output (function return) data type for printCourseRecord(course) ? none


#%%
###################################### Question 7 ###############################
# write a function (with arguement of courses) to print out the complete transcript and the gpa at the end
# 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A-  Grade point credits: 14.80 
# ........  few more lines
# Cumulative GPA: ?????
 
def printTranscript(courses):
  # write an appropriate and helpful docstring
  '''
  Print transcript
  :param float: gpa
  :param str: all classes on transcript 
  :return: none
  '''
  for course in courses:
    # print out each record as before
  
  # after the completion of the loop, print out a new line with the gpa info
  
    return # or return None

# Try to run, see if it works as expected to produce the desired result
# courses is already definted in Q4
printTranscript(courses)
# The transcript should exactly look like this: 
# 2020 spring - DATS 6101 : Intro to DS (3 credits) B- Grade point credits: 8.10
# 2020 fall - DATS 6102 : Data Warehousing (4 credits) A- Grade point credits: 14.80
# 2020 spring - DATS 6103 : Intro Data Mining (3 credits) A Grade point credits: 12.00
# 2020 fall - DATS 6202 : Machine Learning I (4 credits) B+ Grade point credits: 13.20
# 2021 spring - DATS 6203 : Machine Learning II (4 credits) A- Grade point credits: 14.80
# 2021 spring - DATS 6401 : Visualization (3 credits) C+ Grade point credits: 6.90
# 2021 fall - DATS 6101 : Capstone (3 credits) A- Grade point credits: 11.10
# Cumulative GPA: 3.37

# What is the input (function argument) data type for printTranscript? float
# What is the output (function return) data type for printTranscript(courses) ? none



#%% 
# ######  QUESTION 8   Recursive function   ##########
# Write a recursive function that calculates the Fibonancci sequence.
# The recusive relation is fib(n) = fib(n-1) + fib(n-2), 
# and the typically choice of seed values are fib(0) = 0, fib(1) = 1. 
# From there, we can build fib(2) and onwards to be 
# fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, ...
# Let's set it up from here:
import math

def fib(n):
  """
  Finding the Fibonacci sequence with seeds of 0 and 1
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is fib(n) = fib(n-1) + fib(n-2)
  :param n: the index, starting from 0
  :return: the sequence
  """
  # assume n is positive integer
  n = math.floor(n)
  # ??????    fill in your codes here

  return n + fib(n-1) + fib(n-2)



# Try:
for i in range(12):
  print(fib(i))  



#%% 
# ######  QUESTION 9   Recursive function   ##########
# Similar to the Fibonancci sequence, let us create one (say dm_fibonancci) that has a  
# modified recusive relation dm_fibonancci(n) = dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3). 
# Pay attention to the coefficients and their signs. 
# And let us choose the seed values to be dm_fibonancci(0) = 1, dm_fibonancci(1) = 1, dm_fibonancci(2) = 2. 
# From there, we can build dm_fibonancci(3) and onwards to be 1,1,2,3,6,10,...
# Let's set it up from here:

import math

def dm_fibonancci(n):
  """
  Finding the dm_Fibonacci sequence with seeds of 1, 1, 2 for n = 0, 1, 2 respectively
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is dm_fibonancci(n) = dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3)
  :param n: the index, starting from 0
  :return: the sequence
  """
  # assume n is positive integer
  
  n = math.floor(n)
  
  # ??????    fill in your codes here

  return n + dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3)

for i in range(12):
  print(dm_fibonancci(i))  # should gives 1,1,2,3,6,10,...


#%%

