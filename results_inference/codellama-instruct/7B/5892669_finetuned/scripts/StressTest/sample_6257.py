discount_premise = 20
discount_hypothesis = 50
money_saved_premise = 4
money_saved_hypothesis = 4

# the hypothesis refers to the discount and money saved mentioned in the premise
if discount_premise!= discount_hypothesis:
    # check if the discount percentage in the hypothesis contradicts the discount percentage reported in the premise
    label = "contradiction"
elif money_saved_hypothesis!= money_saved_premise:
    # check if the money saved in the hypothesis contradicts the money saved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
