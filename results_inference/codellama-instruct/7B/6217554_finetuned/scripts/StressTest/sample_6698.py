withdrawal_amount_premise = 2000
withdrawal_amount_hypothesis = 7000

if withdrawal_amount_hypothesis!= withdrawal_amount_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
