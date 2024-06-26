capital_premise = 300
capital_hypothesis = 300

# the hypothesis refers to James' capital mentioned in the premise
if capital_hypothesis >= capital_premise:
    # check if the estimate of 'capital_hypothesis' contradicts the exact amount of capital in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
