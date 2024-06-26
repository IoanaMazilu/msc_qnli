candy_pieces_premise = 47.0
candy_pieces_first_night_premise = 25.0
candy_pieces_given_premise = 40.0
candy_pieces_hypothesis = 65.0

# the hypothesis refers to the total number of candy pieces, which are also mentioned in the premise
# compute the total number of candy pieces in the premise
total_candy_pieces_premise = candy_pieces_premise + candy_pieces_first_night_premise + candy_pieces_given_premise
if candy_pieces_hypothesis!= total_candy_pieces_premise:
    # check if the number of candy pieces in the hypothesis contradicts the number of candy pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
