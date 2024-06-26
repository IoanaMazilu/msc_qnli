combinations_premise = 55
combinations_hypothesis = 65

# the hypothesis refers to the number of combinations in which Michael is not selected, also mentioned in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif combinations_premise != combinations_hypothesis:
    # the hypothesis value is greater than the premise value, but it doesn't contradict the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
