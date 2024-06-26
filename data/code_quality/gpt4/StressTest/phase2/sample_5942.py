gangs_premise = 5
gangs_hypothesis = 5

# the hypothesis refers to the number of Mala's gangs mentioned in the premise
if gangs_hypothesis > gangs_premise:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
