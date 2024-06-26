amount_premise = 3600
amount_hypothesis = 1600
interest_rate = 6

# the hypothesis refers to the amount from Anwar and the interest rate mentioned in the premise
if amount_premise <= amount_hypothesis:
    # check if the estimate of 'amount_hypothesis' contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
