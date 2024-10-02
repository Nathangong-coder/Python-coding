#Nathan Gong
#EPS Spring Trimester
#3/23/2022
# Programming 1
#Class 3 Homework-Calculating Course Grades

#Step 1-variables_statement
Responsible_Action=5
Classwork_and_Homework=35
Midterm_Quiz=15
Final_Project=25
Midterm_Project=20

#Step 2-Calculation & Display
#Regular Work Display
regular_work_display='The total of all regular work is'
regular_work_percentage=Responsible_Action+Classwork_and_Homework
regular_work_display2='percent'
#Major Assignment Display
major_assignment_display='The total of all major assignments is'
major_assignment_percentage=Midterm_Quiz+Final_Project+Midterm_Project
major_assignment_display2='percent'
#All Grade Display
all_grade_display='The total of all graded categories is'
all_grade_percentage=Responsible_Action+Classwork_and_Homework+Midterm_Quiz+Final_Project+Midterm_Project
all_grade_display2='percent'
#printing of the displays
print(regular_work_display,regular_work_percentage,regular_work_display2)
print(major_assignment_display,major_assignment_percentage,major_assignment_display2)
print(all_grade_display,all_grade_percentage,all_grade_display2)


#Step 3-Grade Input on each category
#Common Display to start all messages and displays here
each_category_messages_display='In a hypothetical world...'
hypothetical_if_then_display='If I get a'
#hypothetical grades
responsible_action_grade=85
classwork_homework_grade=90
midterm_quiz_grade=95
midterm_project_grade=96
final_project_grade=97
#Display of each section of my hypothetical grade
responsible_action_display='on my responsible action grade'
classwork_homework_display='on my classwork and homework grade'
midterm_quiz_display='on my midterm quiz grade'
midterm_project_display='on my midterm project grade'
final_project_display='on my final project grade'
#printing all my work
print(each_category_messages_display)
print(hypothetical_if_then_display,responsible_action_grade,responsible_action_display)
print(hypothetical_if_then_display,classwork_homework_grade,classwork_homework_display)
print(hypothetical_if_then_display,midterm_quiz_grade,midterm_project_display)
print(hypothetical_if_then_display,midterm_project_grade,midterm_project_display)
print(hypothetical_if_then_display,final_project_grade,final_project_display)
#Step 4-
#Display to introduction the calculations and messages
average_regular_work_display_introduction='I would average'
average_major_assignment_display_introduction='I would average'
average_wholegrade_display_introduction='...And my final grade would be'
#Math for the regular work, major assignments, and the total grade 
#I divided by regular_work_percentage since I'm not weighting them based on all 100 percent of grades.
regular_work_grade_math=(responsible_action_grade/regular_work_percentage*Responsible_Action+classwork_homework_grade/regular_work_percentage*Classwork_and_Homework)
major_assignment_grade_math=(midterm_quiz_grade/major_assignment_percentage*Midterm_Quiz+midterm_project_grade/major_assignment_percentage*Midterm_Project+final_project_grade/major_assignment_percentage*Final_Project)
final_grade_math=(regular_work_grade_math/all_grade_percentage*regular_work_percentage+major_assignment_grade_math/all_grade_percentage*major_assignment_percentage)
#Display to finish labelling/explaining my calculations
average_regular_work_label_display='on regular work'
average_major_work_label_display='on major assessment work'
#Prnting all my work
print(average_regular_work_display_introduction,regular_work_grade_math,average_regular_work_label_display)
print(average_major_assignment_display_introduction,major_assignment_grade_math,average_major_work_label_display)
print(average_wholegrade_display_introduction,final_grade_math)