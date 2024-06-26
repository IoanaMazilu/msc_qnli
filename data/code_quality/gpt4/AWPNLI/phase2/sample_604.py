blocks_randy_premise = 78.0
blocks_received_premise = 19.0
total_blocks_hypothesis = 97.0

# the hypothesis refers to the number of blocks, which are also mentioned in the premise
# compute the total number of blocks in the premise
total_blocks_premise = blocks_randy_premise + blocks_received_premise
if total_blocks_hypothesis != total_blocks_premise:
    # check if the number of blocks in the hypothesis contradicts the number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
