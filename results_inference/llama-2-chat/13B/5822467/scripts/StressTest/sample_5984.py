students_grade_premise = 25
students_grade_hypothesis = 85

# the hypothesis refers to the percentage of students at Morse with cars, mentioned in the premise
if students_grade_premise <= students_grade_hypothesis:
    # check if the estimate of'students_grade_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
elif students_grade_hypothesis!= students_grade_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage of students with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
