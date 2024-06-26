terrorists_premise = 700
families_premise = 700

# the premise and hypothesis mention the same number of people and their families fleeing Syria for Turkey
if terrorists_hypothesis == terrorists_premise:
    # if the number of terrorists and their families in the hypothesis matches the premise, we can infer entailment
    label = "entailment"
elif terrorists_hypothesis < terrorists_premise:
    # if the number of terrorists and their families in the hypothesis is less than the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
