vehicles_value_premise = 1000000
vehicles_value_hypothesis = 1000000

# the hypothesis mentions the value of the stolen vehicles, which is also mentioned in the premise
if vehicles_value_hypothesis!= vehicles_value_premise:
    # check if the value of the vehicles in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
