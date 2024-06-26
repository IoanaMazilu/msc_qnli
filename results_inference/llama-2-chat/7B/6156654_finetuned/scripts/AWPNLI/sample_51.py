fresh_fruit_sold_premise = 9792.0
frozen_fruit_sold_premise = 3513.0
fresh_fruit_sold_hypothesis = 6280.0

# the hypothesis refers to the total pounds of fresh fruit sold, which can be calculated from the premise
if fresh_fruit_sold_hypothesis!= fresh_fruit_sold_premise:
    # check if the amount of fresh fruit sold in the hypothesis contradicts the amount of fresh fruit sold in the premise
    label = "contradiction"
else:
    # if the amount of fresh fruit sold in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
