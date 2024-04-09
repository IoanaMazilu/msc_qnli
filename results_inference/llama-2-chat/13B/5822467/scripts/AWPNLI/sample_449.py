bacteria_premise = 600.0
growth_premise = 8917.0
hypothesis_bacteria = 9513.0

# compute the total number of bacteria in the premise
total_bacteria_premise = bacteria_premise + growth_premise

if hypothesis_bacteria > total_bacteria_premise:
    # the hypothesis implies a larger number of bacteria than the total number of bacteria in the premise, so contradiction
    label = "contradiction"
elif hypothesis_bacteria!= total_bacteria_premise:
    # the hypothesis and the premise have different values for the number of bacteria, so no entailment or contradiction
    label = "neutral"
else:
    # if the hypothesis and the premise have the same value for the number of bacteria, we can infer entailment
    label = "entailment"

print(label)
