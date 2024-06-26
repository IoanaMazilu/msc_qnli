population_premise = 328e6
population_hypothesis = 328e6

# the premise and hypothesis are identical
if population_premise!= population_hypothesis:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
