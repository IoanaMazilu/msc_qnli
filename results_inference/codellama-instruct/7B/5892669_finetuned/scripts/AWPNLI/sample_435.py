initial_amount_premise = 6359.0
spent_amount_premise = 3485.0
remaining_amount_hypothesis = 2870.0

# the hypothesis refers to the remaining amount of money, which is also mentioned in the premise
# compute the remaining amount of money in the premise
remaining_amount_premise = initial_amount_premise - spent_amount_premise
if remaining_amount_hypothesis!= remaining_amount_premise:
    # check if the remaining amount in the hypothesis contradicts the remaining amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
