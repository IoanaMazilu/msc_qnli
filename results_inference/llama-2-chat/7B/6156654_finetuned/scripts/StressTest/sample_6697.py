withdrawal_amount_premise = 5000
withdrawal_amount_hypothesis = 2000

# the hypothesis refers to the withdrawal amount, which is also mentioned in the premise
if withdrawal_amount_hypothesis >= withdrawal_amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it entails the premise
    label = "entailment"

print(label)
