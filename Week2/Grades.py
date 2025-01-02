import csv
   # Subject Average Calculation
   # Accurately calculates average grades for Math, Science, and English
   # Correctly applies arithmetic operations for averaging

math_scores = []  # To store math scores
science_scores = []  # To store science scores
english_scores = []  # To store English scores

def subject_averages(filename):
    with open(filename) as subjects:
        subjects_data = csv.reader(subjects)
        next(subjects_data)  # Skip the header row 

        for row in subjects_data:  # Iterate through rows
            try: 
                math_scores.append(int(row[1]))
            except ValueError: 
                math_scores.append(0)
            try:
                science_scores.append(int(row[2]))
            except ValueError: 
                science_scores.append(0)
            try: 
                english_scores.append(int(row[3]))
            except ValueError:
                english_scores.append(0)

        # Calculate averages after processing all rows
        math_avg = sum(math_scores) / len(math_scores) 
        science_avg = sum(science_scores) / len(science_scores) 
        english_avg = sum(english_scores) / len(english_scores)

        # Check for invalid values

        if math_avg == 0: 
            print("Invalid value in Math column") 
        if science_avg == 0: 
            print("Invalid value in Science column")
        if english_avg == 0: 
            print("Invalid value in English column")

        return f"Math: {math_avg}, Science: {science_avg}, English: {english_avg}"

# Highest Overall Grade Identification
def highest_grade (filename):
    with open(filename) as grades: 
        grades_data = csv.reader(grades)
        next(grades_data)  #skips the header row 

        highest_grade = 0 # variable to store the highest grade 
        top_student = "" # variable to store the student w/the highest grade 
      

        for row in grades_data: # for loop to iterate through the rows or student's and their grades
            try: 
                math = int(row[1])
            except ValueError: 
                math = 0
            try:
                science = int(row[2])
            except ValueError: 
                science = 0
            try: 
                english = int(row[3])
            except ValueError:
                english = 0 
            

            student_avg = math + science + english / 3 
            
            if student_avg > highest_grade: # conditional to check if the student's average is the highest
                highest_grade = student_avg
                top_student = row[0]
        if math == 0:
            print("Invalid value in Math column")
        if science == 0:
            print("Invalid value in Science column")
        if english == 0:
            print("Invalid value in English column")
            
        return top_student

# Highest Average Subject Determination
# Identifies the subject with the highest overall average grade
def highest_overall(filename):
    with open(filename) as subjects:
        subjects_data = csv.reader(subjects)
        next(subjects_data)  # Skip the header row 

        for row in subjects_data:  # Iterate through rows
            try: 
                math_scores.append(int(row[1]))
            except ValueError: 
                math_scores.append(0)
            try:
                science_scores.append(int(row[2]))
            except ValueError: 
                science_scores.append(0)
            try: 
                english_scores.append(int(row[3]))
            except ValueError:
                english_scores.append(0)
               
        
        # Calculate averages after processing all rows
        math_avg2 = sum(math_scores) / len(math_scores) 
        science_avg2 = sum(science_scores) / len(science_scores) 
        english_avg2 = sum(english_scores) / len(english_scores) 

        # Check for invalid values
        if math_avg2 == 0: 
            print("Invalid value in Math column") 
        if science_avg2 == 0: 
            print("Invalid value in Science column")
        if english_avg2 == 0: 
            print("Invalid value in English column")
            
        highest_subject_avg = max(math_avg2, science_avg2, english_avg2)  # Return the highest average
        return f"The highest subject is {'Math' if highest_subject_avg == math_avg2 else 'Science' if highest_subject_avg == science_avg2 else 'English'} with an average of {highest_subject_avg}"

print(subject_averages("student_grades.csv"))
print(highest_grade("student_grades.csv"))
print(highest_overall("student_grades.csv"))
