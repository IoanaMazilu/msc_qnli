people_executed_premise = 420
population_premise = 4.4e6
population_hypothesis = 4.4e6

# the hypothesis talks about the population of Singapore, which is also mentioned in the premise
if population_hypothesis != population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
