cost_price_premise = 100  # represent the cost price of the cupboard in the premise
discount_premise = 62  # represent the discount percentage in the premise
cupboard_sold_premise = cost_price_premise * (1 - discount_premise/100)  # calculate the sold price of the cupboard in the premise

cupboard_sold_hypothesis = cost_price_premise * (1 - 12/100)  # calculate the sold price of the cupboard in the hypothesis

# check if the sold price in the hypothesis is less than or equal to the sold price in the premise
if cupboard_sold_hypothesis <= cupboard_sold_premise:
    # the hypothesis is consistent with the premise, so we can infer entailment
    label = "entailment"
elif cupboard_sold_hypothesis > cupboard_sold_premise:
    # the hypothesis contradicts the premise, so we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are equal, we cannot infer entailment or contradiction
    # so we infer neutrality
    label = "neutral"

print(label)
