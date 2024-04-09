population_premise = 69.5
population_hypothesis = 70

# the hypothesis mentions the same percentage of overweight or obese population as the premise
if population_hypothesis == population_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
elif population_hypothesis > population_premise:
    # if the hypothesis value is greater than the premise value, we can infer entailment or contradiction
    label = "entailment"
elif population_hypothesis < population_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values do not match, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
