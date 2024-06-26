population_future_premise = 10e10
population_present_premise = 5.7e9
population_hypothesis = 5.7e9

# the hypothesis talks about the current population which is also mentioned in the premise
if population_hypothesis!= population_present_premise:
    # check if the population in the hypothesis contradicts the population from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
