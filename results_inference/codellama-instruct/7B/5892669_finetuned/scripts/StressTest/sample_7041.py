weight_difference_premise = 10
weight_difference_hypothesis = 40
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference and total weight mentioned in the premise
if weight_difference_hypothesis < weight_difference_premise:
    # check if the estimate of 'weight_difference_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)