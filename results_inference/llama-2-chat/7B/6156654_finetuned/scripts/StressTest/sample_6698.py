withdraw_amount_premise = 2000
withdraw_amount_hypothesis = 7000

# the hypothesis talks about Tony's withdrawal, which is also mentioned in the premise
if withdraw_amount_premise!= withdraw_amount_hypothesis:
    # check if the amount Tony withdraws in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amounts are the same, it's entailment
    label = "entailment"

print(label)
