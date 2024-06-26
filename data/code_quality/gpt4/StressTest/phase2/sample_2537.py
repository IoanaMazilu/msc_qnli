weight_difference_premise = 7
weight_difference_hypothesis = 4
total_weight_premise = 127
total_weight_hypothesis = 127

# the hypothesis talks about the weight difference between Susan and Anna, and their total weight,
# which are also referenced in the premise
if weight_difference_premise != weight_difference_hypothesis:
    # check if the weight difference in the hypothesis contradicts the weight difference reported in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
