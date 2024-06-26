bought_pieces_premise = 900.0
used_pieces_premise = 156.0
total_pieces_hypothesis = 744.0

# the hypothesis refers to the number of pieces of paper left, which are also mentioned in the premise
# compute the total number of pieces of paper in the premise
total_pieces_premise = bought_pieces_premise - used_pieces_premise
if total_pieces_hypothesis!= total_pieces_premise:
    # check if the number of pieces of paper left in the hypothesis contradicts the number of pieces of paper from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
