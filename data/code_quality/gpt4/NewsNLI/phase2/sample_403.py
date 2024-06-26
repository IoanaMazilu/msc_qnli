going_well_premise = 42
going_well_hypothesis = 42

# the hypothesis mentions the percentage of Americans who think things are going well, which is also referenced in the premise
if going_well_hypothesis != going_well_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
