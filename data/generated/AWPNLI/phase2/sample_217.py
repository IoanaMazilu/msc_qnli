# Premise: A candy store has 6.0 boxes of chocolates and each box has 500.0 pieces.
# Hypothesis: 2999.0 pieces are there altogether in the boxes.
# Golden Label: contradiction

boxes_premise = 6.0
pieces_per_box_premise = 500.0
total_pieces_hypothesis = 2999.0

# the hypothesis refers to the total number of pieces, which are also mentioned in the premise
# compute the total number of pieces in the premise
total_pieces_premise = boxes_premise * pieces_per_box_premise
if total_pieces_hypothesis != total_pieces_premise:
    # check if the total number of pieces in the hypothesis contradicts the total number of pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

