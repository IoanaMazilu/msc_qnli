value_premise = 500000000
value_hypothesis = 100000000

# the hypothesis mentions the value of the lost works, which is also mentioned in the premise
if value_hypothesis > value_premise:
    # check if the value in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
elif value_hypothesis < value_premise:
    # check if the value in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
