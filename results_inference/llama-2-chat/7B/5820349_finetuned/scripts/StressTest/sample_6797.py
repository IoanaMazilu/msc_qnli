deposit_premise = 62500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money deposited by Lucy, which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the amount of deposit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
