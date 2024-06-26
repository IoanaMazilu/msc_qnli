kaleb_savings_premise = 21
kaleb_allowance_premise = 15
gambling_wins_premise = 6
current_balance_hypothesis = 220.0

# The hypothesis refers to Kaleb's current balance, which is not mentioned in the premise
# The premise only mentions Kaleb's savings, allowance, and gambling wins

# The hypothesis value is greater than the sum of Kaleb's savings and allowance
if current_balance_hypothesis <= kaleb_savings_premise + kaleb_allowance_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
