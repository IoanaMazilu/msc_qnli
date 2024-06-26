injured_students_premise = 24
injured_students_hypothesis = 25

# the hypothesis mentions the number of badly injured students, which is also mentioned in the premise
if injured_students_hypothesis <= injured_students_premise:
    # check if the number of injured students in the hypothesis contradicts the number of injured students in the premise
    label = "contradiction"
else:
    # if the number of injured students in the hypothesis does not contradict the number of injured students in the premise, we cannot infer entailment or contradiction, so the relation is neutral
    label = "neutral"

print(label)
