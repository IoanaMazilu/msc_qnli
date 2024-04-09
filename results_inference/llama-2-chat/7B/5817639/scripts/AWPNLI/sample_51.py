fresh_pounds_premise = 3513.0
frozen_pounds_premise = 9792.0
fresh_pounds_hypothesis = 6280.0

# compare the number of fresh fruit sold in the hypothesis to the number sold in the premise
if fresh_pounds_hypothesis >= fresh_pounds_premise:
    # if the number of fresh fruit sold in the hypothesis does not contradict the number sold in the premise
    label = "entailment"
elif frozen_pounds_hypothesis!= frozen_pounds_premise:
    # if the number of frozen fruit sold in the hypothesis contradicts the number sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
