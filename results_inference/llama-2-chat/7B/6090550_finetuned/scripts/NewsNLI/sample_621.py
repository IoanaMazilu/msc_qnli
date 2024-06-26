somenumeric_premise = 0.40
somenumeric_hypothesis = 0.40

# the hypothesis mentions the percentage of white males arrested, which is also referenced in the premise
if somenumeric_hypothesis!= somenumeric_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
