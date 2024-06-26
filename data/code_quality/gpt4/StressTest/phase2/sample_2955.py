students_premise = 90
students_hypothesis = 20

# the hypothesis refers to the number of students representing 'x percent' of the boys at the same school mentioned in the premise
if students_hypothesis >= students_premise:
    # check if the estimate of 'students_hypothesis' contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
