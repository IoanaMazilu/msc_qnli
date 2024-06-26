randy_blocks_premise = 78.0
anna_blocks_premise = 19.0
randy_blocks_hypothesis = 102.0

# the hypothesis refers to Randy's blocks, which are also mentioned in the premise
# compute the total number of blocks Randy has in the premise
randy_blocks_total = randy_blocks_premise + anna_blocks_premise
if randy_blocks_total!= randy_blocks_hypothesis:
    # check if the total number of blocks in the premise contradicts the number of blocks in the hypothesis
    label = "contradiction"
else:
    # if the total number of blocks in the premise matches the number of blocks in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
