min_values_premise = 2
min_values_hypothesis = 2
max_values = [-7, -2, -3]
max_value_premise = max(max_values)
max_value_hypothesis = max(max_values)

# the hypothesis refers to the same minimum and maximum values referenced in the premise
if min_values_hypothesis > min_values_premise:
    # check if the estimated 'min_values_hypothesis' contradicts the minimum value in the premise
    label = "contradiction"
elif max_value_hypothesis != max_value_premise:
    # check if the maximum value in the hypothesis contradicts the maximum value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
