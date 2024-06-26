total_rainfall_premise = 25
total_rainfall_hypothesis = 25

# the hypothesis refers to the total rainfall in Springdale mentioned in the premise
if total_rainfall_hypothesis <= total_rainfall_premise:
    # check if the estimate of 'total_rainfall_hypothesis' contradicts the total rainfall in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
