investment_premise = 1000000000
investment_hypothesis = 5000000000

# the hypothesis refers to the invested amount mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the premise investment value contradicts the estimate of less than 'investment_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
