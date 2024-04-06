# Premise: Christian’s father and the senior ranger gathered firewood as they walked towards the lake in the park and brought with them sacks, and every sack can contain around 20.0 pieces of wood.
# Hypothesis: They were able to fill 6.0 sacks if they gathered 80.0 pieces of wood.
# Golden Label: contradiction

pieces_per_sack = 20.0
gathered_pieces_hypothesis = 80.0
filled_sacks_hypothesis = 6.0

# the hypothesis refers to the number of pieces of wood and filled sacks, which are related to the premise
# compute the total number of sacks based on the gathered wood pieces in the hypothesis
total_sacks_hypothesis = gathered_pieces_hypothesis / pieces_per_sack
if total_sacks_hypothesis != filled_sacks_hypothesis:
    # check if the number of filled sacks in the hypothesis contradicts the number of sacks based on gathered wood pieces
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

