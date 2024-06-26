money_given_premise = 40
money_given_hypothesis = 70

# the hypothesis refers to the percentage of money Jones gave to his wife, mentioned in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the estimate of'money_given_hypothesis' contradicts the percentage of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
