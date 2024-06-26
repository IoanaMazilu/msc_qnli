population_future_premise = 10e9
population_current_premise = 5.7e9
population_current_hypothesis = 5.7e9

# the hypothesis talks about the current population of the world, which is also mentioned in the premise
if population_current_hypothesis != population_current_premise:
    # check if the current population in the hypothesis contradicts the current population from the premise
    label = "contradiction"
else:
    # if the current population in the hypothesis does not contradict the current population from the premise, we can infer entailment
    label = "entailment"

print(label)
