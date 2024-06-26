pieces_per_sack_premise = 20.0
total_pieces_premise = 80.0
filled_sacks_hypothesis = 6.0

# the hypothesis refers to the number of sacks filled with wood, which is also mentioned in the premise
# compute the total number of sacks filled with wood in the premise
filled_sacks_premise = total_pieces_premise / pieces_per_sack_premise
if filled_sacks_hypothesis!= filled_sacks_premise:
    # check if the number of sacks in the hypothesis contradicts the number of sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
