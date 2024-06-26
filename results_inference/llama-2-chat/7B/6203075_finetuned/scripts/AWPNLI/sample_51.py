total_pounds_sold_premise = 9792.0
frozen_pounds_sold_premise = 3513.0
fresh_pounds_sold_hypothesis = 6280.0

# the hypothesis refers to the total pounds of fresh fruit sold, which is also mentioned in the premise
# compute the total pounds of fresh fruit sold according to the hypothesis
total_pounds_fresh_sold_premise = total_pounds_sold_premise - frozen_pounds_sold_premise
if fresh_pounds_sold_hypothesis!= total_pounds_fresh_sold_premise:
    # check if the total pounds of fresh fruit sold in the hypothesis contradicts the total pounds of fresh fruit sold according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
