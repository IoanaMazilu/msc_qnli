blocks_premise = float(78.0)
blocks_hypothesis = float(102.0)

# compare the number of blocks given in the premise and hypothesis
if blocks_hypothesis >= blocks_premise:
    # check if the number of blocks in the hypothesis contradicts the estimate of blocks given in the premise
    label = "contradiction"
elif blocks_hypothesis - blocks_premise > 0:
    # if the number of blocks in the hypothesis is greater than the estimate of blocks given in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
