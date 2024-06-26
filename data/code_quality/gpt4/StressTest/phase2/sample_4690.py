susan_weight_diff_premise = 62
susan_weight_diff_hypothesis = 12
total_weight_premise = 162
total_weight_hypothesis = 162

# the hypothesis refers to the difference in weight between Susan and Anna and their total weight mentioned in the premise
if susan_weight_diff_hypothesis >= susan_weight_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'susan_weight_diff_premise'
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
