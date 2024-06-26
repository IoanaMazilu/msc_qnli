rate_premise = 100
rate_hypothesis = 400

# the hypothesis refers to the driving rate of Molly and Max mentioned in the premise
if rate_premise >= rate_hypothesis:
    # check if the estimate of 'rate_hypothesis' contradicts the driving rate in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
