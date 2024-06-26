jones_money_given_premise = 40
jones_money_given_hypothesis = 60

# the hypothesis refers to the percentage of money Jones gave to his wife, which is also mentioned in the premise
if jones_money_given_premise >= jones_money_given_hypothesis:
    # check if the percentage of money given in the premise contradicts the hypothesis estimate of less than 'jones_money_given_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
