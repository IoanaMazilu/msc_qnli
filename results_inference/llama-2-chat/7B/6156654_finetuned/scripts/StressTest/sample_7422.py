floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the same event as the premise, but with different floor numbers and rates
if floor_hypothesis <= floor_premise:
    # check if the hypothesis floor number contradicts the floor number in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
