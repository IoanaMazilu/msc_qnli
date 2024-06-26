money_given_premise = 40
money_given_hypothesis = 60

# the hypothesis refers to the percentage of money Jones gave to his wife, mentioned in the premise
if money_given_premise >= money_given_hypothesis:
    # check if the percentage of money given in the premise contradicts the estimate of'money_given_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
