capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to James' capital, which is also mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the premise value contradicts the estimate of less than 'capital_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
