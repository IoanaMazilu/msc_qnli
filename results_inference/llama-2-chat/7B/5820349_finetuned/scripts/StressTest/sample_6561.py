average_raise_premise = 2
average_raise_hypothesis = 6

# the hypothesis refers to the points Jerry wants to raise his average by, which is also mentioned in the premise
if average_raise_hypothesis <= average_raise_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
