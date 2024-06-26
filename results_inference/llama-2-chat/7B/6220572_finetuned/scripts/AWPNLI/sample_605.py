blocks_premise = 78.0
blocks_given_premise = 19.0
blocks_hypothesis = 102.0

# the hypothesis talks about the total number of blocks, which are also referenced in the premise
# compute the total number of blocks in the premise
total_blocks_premise = blocks_premise + blocks_given_premise
if blocks_hypothesis!= total_blocks_premise:
    # check if the number of blocks in the hypothesis contradicts the number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
