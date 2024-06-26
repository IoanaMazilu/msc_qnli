total_fruit_premise = 9792.0
frozen_fruit_premise = 3513.0
fresh_fruit_hypothesis = 6280.0

# the hypothesis refers to the quantity of fresh fruit, which can be inferred from the premise
# compute the quantity of fresh fruit in the premise
fresh_fruit_premise = total_fruit_premise - frozen_fruit_premise

if fresh_fruit_hypothesis != fresh_fruit_premise:
    # check if the quantity of fresh fruit in the hypothesis contradicts the quantity of fresh fruit from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
