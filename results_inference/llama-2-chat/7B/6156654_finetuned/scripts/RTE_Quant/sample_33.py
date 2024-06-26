population_premise = 10_000_000_000
population_hypothesis = 5_700_000_000

# The hypothesis refers to the current world population, which is also mentioned in the premise
if population_hypothesis!= population_premise:
    # If the population in the hypothesis is not the same as the population in the premise, then it is a contradiction
    label = "contradiction"
else:
    # If the population in the hypothesis is the same as the population in the premise, then it is an entailment
    label = "entailment"

print(label)
