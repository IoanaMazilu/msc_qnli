discount_premise = 20
discount_hypothesis = 30
money_saved_premise = 4
money_saved_hypothesis = 4

# the hypothesis refers to the discount percentage and money saved mentioned in the premise
if discount_hypothesis < discount_premise:
    # check if the 'discount_hypothesis' contradicts the discount percentage in the premise
    label = "contradiction"
elif money_saved_hypothesis!= money_saved_premise:
    # check if the money saved in the hypothesis contradicts the money saved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
