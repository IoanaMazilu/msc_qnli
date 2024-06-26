share_value_premise = 1300
share_value_hypothesis = 1300

# the hypothesis refers to the same share value mentioned in the premise
if share_value_hypothesis >= share_value_premise:
    # check if the estimate of'share_value_hypothesis' contradicts the share value in the premise
    label = "contradiction"
elif share_value_hypothesis < share_value_premise:
    # check if the share value in the hypothesis is less than the share value in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
