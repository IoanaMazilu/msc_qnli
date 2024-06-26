family_moved_premise = True
money_converted_premise = True
checking_account_premise = 6359.0
spent_money_premise = 3485.0
total_money_premise = checking_account_premise - spent_money_premise
hypothesis_premise = 2870.0

# the hypothesis refers to the amount of money left, which is also mentioned in the premise
# compute the total amount of money left in the premise
total_money_hypothesis = total_money_premise - hypothesis_premise
if total_money_hypothesis < 0:
    # check if the amount of money left in the hypothesis is negative
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
