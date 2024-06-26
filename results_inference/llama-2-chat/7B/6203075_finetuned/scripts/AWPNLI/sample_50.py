fresh_fruit_sold_premise = 9792.0
frozen_fruit_sold_premise = 3513.0
fresh_fruit_sold_hypothesis = 6279.0

# the hypothesis refers to the amount of fresh fruit sold, which is also mentioned in the premise
# compute the amount of fresh fruit sold in the premise
fresh_fruit_sold_premise_quantity = fresh_fruit_sold_premise - frozen_fruit_sold_premise
if fresh_fruit_sold_hypothesis!= fresh_fruit_sold_premise_quantity:
    # check if the amount of fresh fruit sold in the hypothesis contradicts the amount sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
