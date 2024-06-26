blocks_randy_premise = 78.0
blocks_given_premise = 19.0
blocks_randy_hypothesis = 102.0

# the hypothesis refers to the number of blocks Randy has, which are also mentioned in the premise
# compute the total number of blocks Randy has in the premise
total_blocks_premise = blocks_randy_premise + blocks_given_premise
if blocks_randy_hypothesis!= total_blocks_premise:
    # check if the number of blocks in the hypothesis contradicts the number of blocks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
