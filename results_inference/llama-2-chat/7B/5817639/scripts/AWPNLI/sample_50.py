fresh_sold_premise = 3513.0
fresh_sold_hypothesis = 6279.0

# check if the number of fresh fruit sold in the hypothesis contradicts the number of fresh fruit sold in the premise
if fresh_sold_hypothesis > fresh_sold_premise:
    label = "contradiction"
elif fresh_sold_hypothesis < fresh_sold_premise:
    # check if the number of fresh fruit sold in the hypothesis is less than the number of fresh fruit sold in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
