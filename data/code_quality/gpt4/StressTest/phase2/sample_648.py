innings_premise = 16
innings_hypothesis = 86

# the hypothesis refers to the number of innings mentioned in the premise
if innings_hypothesis <= innings_premise:
    # check if the hypothesis value contradicts the number of innings in the premise
    label = "contradiction"
elif innings_hypothesis == innings_premise:
    # if the hypothesis value and premise ones are the same, we can infer entailment
    label = "entailment"
else:
    # the premise does not contradict the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
