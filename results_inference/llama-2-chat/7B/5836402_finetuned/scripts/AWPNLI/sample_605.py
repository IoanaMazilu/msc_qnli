blocks_randy_premise = 78.0
blocks_anna_premise = 19.0
total_blocks_hypothesis = 102.0

# the hypothesis refers to the total number of blocks, which are also mentioned in the premise
# compute the total number of blocks in the premise
total_blocks_premise = blocks_randy_premise + blocks_anna_premise
if total_blocks_hypothesis!= total_blocks_premise:
    # check if the total number of blocks in the hypothesis contradicts the total number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)