fresh_fruit_sold_premise = 9792.0
frozen_fruit_sold_premise = 3513.0
fresh_fruit_sold_hypothesis = 6279.0

# the hypothesis refers to the amount of fresh fruit sold, which is also mentioned in the premise
# compute the amount of fresh fruit sold in the premise
fresh_fruit_sold_premise_computed = fresh_fruit_sold_premise - frozen_fruit_sold_premise

# check if the amount of fresh fruit sold in the hypothesis contradicts the amount of fresh fruit sold in the premise
if fresh_fruit_sold_hypothesis!= fresh_fruit_sold_premise_computed:
    label = "contradiction"
else:
    label = "entailment"

print(label)
