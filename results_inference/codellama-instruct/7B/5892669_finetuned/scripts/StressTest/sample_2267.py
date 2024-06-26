gloves_premise = 20
gloves_hypothesis = 20

# the hypothesis refers to the number of pairs of matched gloves mentioned in the premise
if gloves_hypothesis >= gloves_premise:
    # check if the hypothesis value contradicts the number of gloves in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
