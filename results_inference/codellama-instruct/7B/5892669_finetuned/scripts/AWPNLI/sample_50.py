total_fresh_fruit_premise = 9792.0
total_frozen_fruit_premise = 3513.0
fresh_fruit_hypothesis = 6279.0

# the hypothesis refers to the number of fresh fruit, which is also mentioned in the premise
# compute the total number of fresh fruit in the premise
total_fresh_fruit_premise = total_fresh_fruit_premise - total_frozen_fruit_premise
if fresh_fruit_hypothesis!= total_fresh_fruit_premise:
    # check if the number of fresh fruit in the hypothesis contradicts the number of fresh fruit from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)