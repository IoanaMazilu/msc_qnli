susan_weight_difference_premise = 10
susan_weight_difference_hypothesis = 40
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis talks about the weight difference between Susan and Anna, referenced also in the premise
if susan_weight_difference_hypothesis < susan_weight_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than'susan_weight_difference_premise'
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference
    # any weight difference less than'susan_weight_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
