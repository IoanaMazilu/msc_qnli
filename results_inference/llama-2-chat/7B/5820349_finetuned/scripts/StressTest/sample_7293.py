capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to the value of James' capital mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the value of 'capital_premise' contradicts the estimate of less than 'capital_hypothesis'
    label = "contradiction"
else:
    # if the value of 'capital_premise' is less than 'capital_hypothesis', we can infer entailment
    label = "entailment"

print(label)
