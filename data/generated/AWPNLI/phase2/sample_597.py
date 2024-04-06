# Premise: Adolfo made a tower with 35.0 blocks and he added 65.0 more blocks to the tower.
# Hypothesis: 101.0 total blocks are in the tower now.
# Golden Label: contradiction

initial_blocks_premise = 35.0
added_blocks_premise = 65.0
total_blocks_hypothesis = 101.0

# the hypothesis refers to the total number of blocks in the tower, which are also mentioned in the premise
# compute the total number of blocks in the premise
total_blocks_premise = initial_blocks_premise + added_blocks_premise
if total_blocks_hypothesis != total_blocks_premise:
    # check if the total number of blocks in the hypothesis contradicts the total number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

