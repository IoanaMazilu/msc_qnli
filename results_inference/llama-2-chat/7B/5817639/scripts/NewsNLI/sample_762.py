value_premise = 50000000
value_hypothesis = 10000000

# the hypothesis mentions a lower value for the lost works than the premise
if value_hypothesis < value_premise:
    # check if the value in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis value is lower than the premise value, we can infer entailment
    label = "entailment"

print(label)
