world_population_premise = 10e9
world_population_hypothesis = 5.7e9

# the hypothesis talks about the current world population, which is also mentioned in the premise
if world_population_hypothesis!= world_population_premise:
    # check if the current population in the hypothesis contradicts the current population in the premise
    label = "contradiction"
else:
    # if the hypothesis value and premise value are the same, we can infer entailment
    label = "entailment"

print(label)
