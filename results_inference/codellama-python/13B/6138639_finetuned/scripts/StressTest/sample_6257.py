discount_premise = 20
discount_hypothesis = 50
price_difference_premise = 4
price_difference_hypothesis = 4

# the hypothesis talks about the discount and the price difference, both referenced in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif price_difference_hypothesis!= price_difference_premise:
    # check if the price difference in the hypothesis contradicts the price difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
