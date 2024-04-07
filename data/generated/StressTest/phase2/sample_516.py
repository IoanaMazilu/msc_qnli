# Premise: Luckily Sarah negotiated a 20% discount for the present so that each of them paid 4 dollars less.
# Hypothesis: Luckily Sarah negotiated a less than 80% discount for the present so that each of them paid 4 dollars less.
# Golden Label: entailment

discount_premise = 20
discount_hypothesis = 80
saved_money_premise = 4
saved_money_hypothesis = 4

# the hypothesis refers to the discount and money saved mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount in the premise
    label = "contradiction"
elif saved_money_hypothesis != saved_money_premise:
    # check if the money saved in the hypothesis contradicts the money saved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

