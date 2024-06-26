total_pounds_premise = 9792.0
frozen_pounds_premise = 3513.0
fresh_pounds_hypothesis = 6280.0

# the hypothesis refers to the total pounds of fresh fruit sold, which is also mentioned in the premise
# compute the total pounds of fresh fruit sold in the premise
total_fresh_pounds_premise = total_pounds_premise - frozen_pounds_premise
if fresh_pounds_hypothesis!= total_fresh_pounds_premise:
    # check if the hypothesis value contradicts the value of total fresh fruit sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
