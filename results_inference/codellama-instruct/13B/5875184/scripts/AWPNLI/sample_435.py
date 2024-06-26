premise_money_converted = 6359.0
premise_spent_money = 3485.0
hypothesis_left_money = 2870.0

# the hypothesis refers to the amount of money left, which is also mentioned in the premise
# compute the total amount of money spent by the family
total_spent_money = premise_spent_money + premise_money_converted
if total_spent_money > hypothesis_left_money:
    # check if the amount of money spent contradicts the amount of money left in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
