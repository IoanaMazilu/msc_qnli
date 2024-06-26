deposit_premise = 62500
deposit_hypothesis = 22500
annual_return = 8

# the hypothesis refers to the amount of money deposited by Lucy, mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the amount of deposit in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
# 