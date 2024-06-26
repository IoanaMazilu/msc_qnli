population_premise = 10e9
population_hypothesis = 5.7e9

# the hypothesis talks about the current world population, which is also mentioned in the premise
if population_hypothesis!= population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
