susan_weight_diff_premise = 4
susan_weight_diff_hypothesis = 7
total_weight_premise = 127
total_weight_hypothesis = 127

# the hypothesis talks about the weight difference between Susan and Anna, and their total weight, referenced also in the premise
if total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
elif susan_weight_diff_hypothesis <= susan_weight_diff_premise:
    # check if the weight difference between Susan and Anna mentioned in the hypothesis contradicts the estimate of more than 'susan_weight_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference between Susan and Anna
    # any weight difference greater than 'susan_weight_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
