#TASK 1
#Calculating Average

grades = [2, 14, 57, 44, 95, 84, 31, 58, 84, 0]

def average_grade(grades):
   total_sum = sum(grades)
   unit = len(grades)
   return (total_sum / unit)

print(average_grade(grades)) #was stuck here for a while. When you call a function that returns a value you HAVE to 'print' in order to show value

#Task 2
#Function to find highest and lowest grade

grades = [2, 14, 57, 44, 95, 84, 31, 58, 84, 0]

def high_low(grades):
   print((max(grades)), 'is the highest grade')
   print((min(grades)), 'is the lowest grade')


(high_low(grades))

#Task 3 BONUS
#Create a feature that categorizes grades into letter grades

grades = [2, 14, 57, 44, 95, 84, 31, 58, 84, 0]

def categorize(grades):
   for grade in grades:
    if 90 <= grade <= 100:  #note the direction of the '<='. had it wrong on first attempt and function does not execute
      print(grade, 'is a A')
    elif 80 <= grade <= 89:
      print(grade, 'is a B')
    elif 70 <= grade <= 79:
      print(grade, 'is a C')
    elif 60 <= grade <= 69:
      print(grade, 'is a D')
    elif 0 <= grade <= 59:
      print(grade, 'is a F')
    
categorize(grades)