fresh_fruit_hypothesis = 6279.0
total_fresh_fruit_premise = 9792.0
total_frozen_fruit_premise = 3513.0

# the hypothesis refers to the amount of fresh fruit sold, which is also mentioned in the premise
# compute the amount of fresh fruit sold in the premise
fresh_fruit_premise = total_fresh_fruit_premise - fresh_fruit_hypothesis
if fresh_fruit_hypothesis!= fresh_fruit_premise:
    # check if the amount of fresh fruit from the hypothesis contradicts the amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
