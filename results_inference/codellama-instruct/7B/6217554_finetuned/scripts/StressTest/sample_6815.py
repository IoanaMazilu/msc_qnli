# define the percentage of students with cars in the premise and hypothesis
percentage_premise = 18
percentage_hypothesis = 58

# define the number of students in the three lower grades in the premise and hypothesis
students_lower_grades_premise = 100
students_lower_grades_hypothesis = 100

# calculate the number of students with cars in the premise and hypothesis
students_with_cars_premise = round(students_lower_grades_premise * percentage_premise / 100)
students_with_cars_hypothesis = round(students_lower_grades_hypothesis * percentage_hypothesis / 100)

# check if the number of students with cars in the hypothesis contradicts the number of students with cars in the premise
if students_with_cars_hypothesis!= students_with_cars_premise:
    label = "contradiction"
# check if the number of students in the three lower grades in the hypothesis contradicts the number of students in the three lower grades reported in the premise
elif students_lower_grades_hypothesis!= students_lower_grades_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
