# Premise: So far, an orchard has sold a combined total of 9792.0 pounds of fresh and frozen fruit this season, and they have sold 3513.0 pounds of frozen fruit.
# Hypothesis: 6279.0 pounds of fresh fruit have been sold so far.
# Golden Label: entailment

total_fruit_sold_premise = 9792.0 
frozen_fruit_sold_premise = 3513.0
fresh_fruit_sold_hypothesis = 6279.0

# the hypothesis refers to the quantity of fresh fruit sold, which can be inferred from the premise
# compute the quantity of fresh fruit sold in the premise
fresh_fruit_sold_premise = total_fruit_sold_premise - frozen_fruit_sold_premise

if fresh_fruit_sold_hypothesis != fresh_fruit_sold_premise:
    # check if the quantity of fresh fruit sold in the hypothesis contradicts the quantity of fresh fruit sold from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

