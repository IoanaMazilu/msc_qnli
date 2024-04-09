fresh_premise = 9792.0 - 3513.0
frozen_premise = 3513.0
fresh_hypothesis = 6279.0

# compute the total amount of fruit sold in the premise
total_premise = fresh_premise + frozen_premise

if fresh_hypothesis > total_premise:
    # check if the amount of fresh fruit in the hypothesis contradicts the estimate of more than 'fresh_premise'
    label = "contradiction"
elif frozen_premise!= fresh_hypothesis:
    # check if the amount of frozen fruit in the hypothesis contradicts the amount of frozen fruit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
