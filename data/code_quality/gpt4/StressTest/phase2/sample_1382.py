reading_rate_premise = 2
reading_rate_hypothesis = 2

# the hypothesis refers to the reading rate mentioned in the premise
if reading_rate_hypothesis > reading_rate_premise:
    # check if the hypothesis value contradicts the exact reading rate given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
