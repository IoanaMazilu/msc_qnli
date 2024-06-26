withdrawal_amount_premise = 2000
withdrawal_amount_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdrawal_amount_premise >= withdrawal_amount_hypothesis:
    # check if the premise value contradicts the estimate of less than 'withdrawal_amount_hypothesis'
    label = "contradiction"
else:
    # if the premise value is less than the hypothesis value, it is entailed
    label = "entailment"

print(label)
