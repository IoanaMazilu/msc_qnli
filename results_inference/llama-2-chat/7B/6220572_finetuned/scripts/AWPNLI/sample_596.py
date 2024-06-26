blocks_tower_premise = 35.0 + 65.0
blocks_hypothesis = 100.0

# the hypothesis refers to the total number of blocks in the tower, which are also mentioned in the premise
# compute the total number of blocks in the premise
total_blocks_premise = blocks_tower_premise
if blocks_hypothesis!= total_blocks_premise:
    # check if the number of blocks in the hypothesis contradicts the number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
