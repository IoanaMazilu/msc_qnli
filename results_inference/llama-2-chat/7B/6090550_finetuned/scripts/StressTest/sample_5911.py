sheep_horses_premise = 6/7
sheep_horses_hypothesis = 1/7
sheep_horses_ratio = 1/7
sheep_horses_needed = 12880

# the hypothesis talks about the ratio of sheep to horses, which is also referenced in the premise
if sheep_horses_hypothesis == sheep_horses_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
elif sheep_horses_hypothesis!= sheep_horses_premise:
    # check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are equal, we can infer entailment
    label = "neutral"

print(label)
