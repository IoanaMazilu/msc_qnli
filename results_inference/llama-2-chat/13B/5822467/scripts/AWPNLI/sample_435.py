abe_family_money_premise = 6359.0
abe_family_spent_premise = 3485.0
left_hypothesis = 2870.0

# compute the total amount of money spent from the premise
total_spent_premise = abe_family_spent_premise + left_hypothesis

if total_spent_premise > left_hypothesis:
    # check if the total amount spent from the premise contradicts the hypothesis
    label = "contradiction"
elif abe_family_money_premise - left_hypothesis < 0:
    # check if the amount left from the hypothesis contradicts the amount left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
