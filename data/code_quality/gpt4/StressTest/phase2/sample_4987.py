weight_difference_premise = 80
weight_difference_hypothesis = 20
total_weight_premise = 160
total_weight_hypothesis = 160

# the hypothesis talks about the weight difference between Susan and Anna, and their total weight, both mentioned in the premise
if weight_difference_hypothesis > weight_difference_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'weight_difference_premise'
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
elif weight_difference_hypothesis < weight_difference_premise:
    # check if the weight difference in the hypothesis is less than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, and cannot be fully entailed, we infer neutrality
    label = "neutral"

print(label)
