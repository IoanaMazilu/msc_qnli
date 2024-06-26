investment_premise = 100000
investment_hypothesis = 600000

# the hypothesis refers to the investment amount mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the investment amount in the hypothesis does not contradict the investment amount in the premise, we can infer entailment
    label = "entailment"

print(label)
