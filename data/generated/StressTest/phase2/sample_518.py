# Premise: Luckily Sarah negotiated a 20% discount for the present so that each of them paid 4 dollars less.
# Hypothesis: Luckily Sarah negotiated a 70% discount for the present so that each of them paid 4 dollars less.
# Golden Label: contradiction

discount_premise = 20
discount_hypothesis = 70
money_saved_premise = 4
money_saved_hypothesis = 4

# the hypothesis refers to the discount and money saved mentioned in the premise
if discount_hypothesis != discount_premise:
    # check if the discount in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
elif money_saved_hypothesis != money_saved_premise:
    # check if the money saved in the hypothesis contradicts the money saved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

