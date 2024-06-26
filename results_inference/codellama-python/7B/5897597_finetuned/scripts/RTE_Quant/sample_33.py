population_future_premise = 10e9
population_current_hypothesis = 5.7e9

# the hypothesis talks about the current world population, which is also mentioned in the premise
if population_current_hypothesis!= population_future_premise:
    # check if the current population in the hypothesis contradicts the future population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
