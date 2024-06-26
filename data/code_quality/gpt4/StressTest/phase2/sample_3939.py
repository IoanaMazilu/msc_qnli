students_premise = 400
students_hypothesis = 500
boys_premise = 0.60
boys_hypothesis = 0.60
girls_premise = 0.80
girls_hypothesis = 0.80

# the hypothesis refers to the number of students who took the exam, and the percentage of boys and girls who cleared the cut off, all mentioned in the premise
if students_hypothesis < students_premise:
    # check if the estimate of 'students_hypothesis' contradicts the number of students in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise or girls_hypothesis != girls_premise:
    # check if the percentage of boys and girls who cleared the cut off in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
