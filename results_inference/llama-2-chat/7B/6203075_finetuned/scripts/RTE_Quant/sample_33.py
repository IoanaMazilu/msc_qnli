population_premise = 10
population_hypothesis = 5.7

# the hypothesis talks about the current world population, which is also mentioned in the premise
if population_hypothesis!= population_premise:
    # check if the current population in the hypothesis contradicts the current population in the premise
    label = "contradiction"
else:
    # if the current population in the hypothesis matches the current population in the premise, we can infer entailment
    label = "entailment"

print(label)
