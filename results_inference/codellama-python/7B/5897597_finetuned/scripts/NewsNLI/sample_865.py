injured_students_premise = 25
injured_students_hypothesis = 25

# the hypothesis mentions the number of injured students, which is also referenced in the premise
if injured_students_hypothesis > injured_students_premise:
    # check if the number of injured students in the hypothesis contradicts the number of injured students reported in the premise
    label = "contradiction"
elif injured_students_hypothesis < injured_students_premise:
    # check if the number of injured students from the hypothesis is less than the number of injured students in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
