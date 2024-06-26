student_grade_premise = 18 / 100
student_grade_hypothesis = 48 / 100

# the hypothesis refers to the percentage of students at Morse with cars
if student_grade_hypothesis <= student_grade_premise:
    # check if the estimate of'student_grade_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif student_grade_hypothesis > student_grade_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage less than 48% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
