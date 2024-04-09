students_premise = 20
percentage_students_premise = 20 / 100
lower_grades_premise = students_premise * percentage_students_premise

hypothesis_lower_grades = lower_grades_premise

# the hypothesis refers to the number of students in the three lower grades
if hypothesis_lower_grades <= lower_grades_premise:
    # check if the estimate of 'lower_grades_premise' contradicts the number of students in the three lower grades in the hypothesis
    label = "contradiction"
elif percentage_students_premise!= hypothesis_lower_grades:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
