total_fruit_premise = 9792.0
frozen_fruit_premise = 3513.0
fresh_fruit_hypothesis = 6279.0

# the hypothesis refers to the amount of fresh fruit sold, which can be calculated from the premise
# compute the amount of fresh fruit sold in the premise
fresh_fruit_premise = total_fruit_premise - frozen_fruit_premise
if fresh_fruit_hypothesis!= fresh_fruit_premise:
    # check if the amount of fresh fruit in the hypothesis contradicts the amount of fresh fruit from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
