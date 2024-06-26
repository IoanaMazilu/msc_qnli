money_premise = 6359.0
money_spent_premise = 3485.0
money_left_hypothesis = 2870.0

# the hypothesis refers to the amount of money left, which is also mentioned in the premise
# compute the remaining money in the premise
remaining_money_premise = money_premise - money_spent_premise

if remaining_money_premise!= money_left_hypothesis:
    # check if the amount of remaining money in the hypothesis contradicts the amount of remaining money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
