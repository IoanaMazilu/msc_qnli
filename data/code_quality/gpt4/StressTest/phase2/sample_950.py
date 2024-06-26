apples_premise = 12
apples_hypothesis = 62

# the hypothesis refers to the number of apples Billy has
if apples_premise != apples_hypothesis:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
