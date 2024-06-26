population_premise = 69.5
population_hypothesis = 69.5

# the hypothesis mentions the same percentage of overweight or obese population as the premise
if population_hypothesis!= population_premise:
    # check if the percentage of overweight or obese population in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
