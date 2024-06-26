ratio_premise = 5/4
ratio_hypothesis = 1/4

# the hypothesis refers to the same ratio as in the premise, but with a different ratio
if ratio_hypothesis == ratio_premise:
    label = "neutral"
elif ratio_hypothesis < ratio_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
