watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis refers to the number of watermelons left with Mike mentioned in the premise
if watermelons_premise >= watermelons_hypothesis:
    # check if the estimate of 'watermelons_hypothesis' contradicts the number of watermelons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
