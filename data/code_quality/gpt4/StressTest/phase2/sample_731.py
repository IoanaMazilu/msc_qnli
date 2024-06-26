pb_premise = 252
pb_hypothesis = 252

# the hypothesis refers to the amount of peanut butter mentioned in the premise
if pb_hypothesis != pb_premise:
    # check if the amount of peanut butter in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
