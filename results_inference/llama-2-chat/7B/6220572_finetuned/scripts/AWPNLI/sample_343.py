firewood_pieces_premise = 80.0
sacks_premise = 6.0
sacks_hypothesis = 6.0

# the hypothesis refers to the number of sacks filled, which is also mentioned in the premise
# compute the number of sacks filled in the premise
sacks_filled_premise = sacks_premise / firewood_pieces_premise
if sacks_hypothesis!= sacks_filled_premise:
    # check if the number of sacks filled in the hypothesis contradicts the number of sacks filled from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
