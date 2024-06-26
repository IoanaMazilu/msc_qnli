joined_months_premise = 8
joined_months_hypothesis = 2

# the hypothesis refers to the time Jose joined, mentioned in the premise
if joined_months_hypothesis < joined_months_premise:
    # check if the estimate of 'joined_months_hypothesis' contradicts the number of months Jose joined in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
