student_grade_premise = 18 / 100 * 100
student_grade_hypothesis = 58 / 100 * 100

# the hypothesis refers to the percentage of students with cars in the three lower grades
if student_grade_hypothesis <= student_grade_premise:
    # check if the estimate of'student_grade_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif student_grade_hypothesis!= student_grade_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
