# Premise: Min (a, b, c) = min of a, b, c Max (a, b, c,) = max of a, b, c then what is the value of MAX { min (2, 5,7), max (-7,-2,-3), 3 }.
# Hypothesis: Min (a, b, c) = min of a, b, c Max (a, b, c,) = max of a, b, c then what is the value of MAX { min (more than 2, 5,7), max (-7,-2,-3), 3 }.
# Golden Label: contradiction

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

