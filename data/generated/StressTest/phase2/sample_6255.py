# Premise: Luckily Saren negotiated a 20% discount for the present so that each of them paid 4 dollars less.
# Hypothesis: Luckily Saren negotiated a less than 30% discount for the present so that each of them paid 4 dollars less.
# Golden Label: entailment

discount_premise = 20
discount_hypothesis = 30
reduction_in_price_premise = 4
reduction_in_price_hypothesis = 4

# the hypothesis refers to the discount and reduction in price mentioned in the premise
if discount_premise > discount_hypothesis:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif reduction_in_price_premise != reduction_in_price_hypothesis:
    # check if the reduction in price in the hypothesis contradicts the reduction in price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

