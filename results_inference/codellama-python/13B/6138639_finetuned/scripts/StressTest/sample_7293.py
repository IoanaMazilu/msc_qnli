capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to the capital of James mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the estimate of 'capital_hypothesis' contradicts the capital in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
