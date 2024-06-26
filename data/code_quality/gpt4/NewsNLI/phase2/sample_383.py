people_died_premise = 4
people_died_hypothesis = 4

# the hypothesis mentions the number of people died in waves, which is also mentioned in the premise
if people_died_hypothesis != people_died_premise:
    # check if the number of people died in the hypothesis contradicts the number of people died reported in the premise
    label = "contradiction"
else:
    # if the number of people died in the hypothesis does not contradict the number of people died in the premise, we can infer entailment
    label = "entailment"

print(label)
