weight_premise = 84
weight_hypothesis = 44

# the hypothesis talks about the weight of butter mixed by Raman
if weight_hypothesis >= weight_premise:
    # check if the weight of butter in the hypothesis contradicts the premise
    label = "contradiction"
elif weight_hypothesis == weight_premise:
    # if the weight of butter in the hypothesis is equal to the premise, we can infer entailment
    label = "entailment"
else:
    # if the weight of butter in the hypothesis is less than the premise, we can infer neutral
    label = "neutral"

print(label)
