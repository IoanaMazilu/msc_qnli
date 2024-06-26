students_premise = 400
students_hypothesis = 400

# the hypothesis refers to the number of students who took the exam mentioned in the premise
if students_hypothesis >= students_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the number of students in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
