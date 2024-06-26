initial_blocks_premise = 35.0
added_blocks_premise = 65.0
total_blocks_hypothesis = 100.0

# the hypothesis refers to the total number of blocks, which is also mentioned in the premise
# compute the total number of blocks in the premise
total_blocks_premise = initial_blocks_premise + added_blocks_premise
if total_blocks_hypothesis!= total_blocks_premise:
    # check if the total number of blocks in the hypothesis contradicts the total number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
