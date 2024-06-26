rate_premise = 100
rate_hypothesis = 100

# the hypothesis refers to the driving rate mentioned in the premise
if rate_premise >= rate_hypothesis:
    # check if the premise value contradicts the estimate of less than 'rate_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
