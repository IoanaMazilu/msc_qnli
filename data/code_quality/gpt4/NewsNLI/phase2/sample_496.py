major_hurricanes_lower_premise = 1
major_hurricanes_upper_premise = 3

major_hurricanes_lower_hypothesis = 1
major_hurricanes_upper_hypothesis = 3

# the hypothesis mentions the number of predicted major hurricanes, which is also referenced in the premise
# we need to check if the range of major hurricanes in the hypothesis contradicts the range in the premise
if major_hurricanes_lower_hypothesis < major_hurricanes_lower_premise or major_hurricanes_upper_hypothesis > major_hurricanes_upper_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
