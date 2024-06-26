money_premise = 6359.0
money_spent_premise = 3485.0
money_left_hypothesis = 2870.0

# the hypothesis refers to the amount of money left, which is also mentioned in the premise
# compute the amount of money left in the premise
money_left_premise = money_premise - money_spent_premise
if money_left_hypothesis!= money_left_premise:
    # check if the amount of money left in the hypothesis contradicts the amount of money left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
