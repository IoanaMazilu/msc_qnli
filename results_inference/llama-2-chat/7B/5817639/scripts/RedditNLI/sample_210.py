raises_premise = 2
hikes_hypothesis = 2

# the premise mentions the number of rate hikes in the current year, while the hypothesis mentions the number of rate hikes in the next year
if hikes_hypothesis!= raises_premise:
    # check if the number of rate hikes in the hypothesis contradicts the number of rate hikes in the premise
    label = "contradiction"
else:
    # if the number of rate hikes in the hypothesis is consistent with the number of rate hikes in the premise, we can infer entailment
    label = "entailment"

print(label)
