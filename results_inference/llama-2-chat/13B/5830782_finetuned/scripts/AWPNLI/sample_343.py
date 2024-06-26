wood_pieces_per_sack_premise = 20.0
gathered_wood_pieces_hypothesis = 80.0
filled_sacks_hypothesis = 6.0

# the hypothesis refers to the number of filled sacks, which is also mentioned in the premise
# compute the number of filled sacks in the premise
filled_sacks_premise = gathered_wood_pieces_hypothesis / wood_pieces_per_sack_premise
if filled_sacks_hypothesis!= filled_sacks_premise:
    # check if the number of filled sacks in the hypothesis contradicts the number of filled sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
