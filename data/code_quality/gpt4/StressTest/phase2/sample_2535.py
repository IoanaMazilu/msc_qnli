weight_difference_premise = 7
weight_difference_hypothesis = 4
total_weight_premise = 127
total_weight_hypothesis = 127

# the hypothesis talks about Susan's weight compared to Anna's and their total weight, both mentioned in the premise
if weight_difference_premise < weight_difference_hypothesis:
    # check if the hypothesis value contradicts the weight difference given in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
