susan_weight_diff_premise = 40
susan_weight_diff_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna, and their total weight, mentioned in the premise
if susan_weight_diff_hypothesis >= susan_weight_diff_premise:
    # check if the weight difference in the hypothesis contradicts the estimate of less than'susan_weight_diff_premise'
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference between Susan and Anna
    # any weight difference less than'susan_weight_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)