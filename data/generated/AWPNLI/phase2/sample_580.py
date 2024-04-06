# Premise: Todd has 54.0 pieces of gum and Steve gave him 16.0 more pieces.
# Hypothesis: Todd has 70.0 pieces of gum now.
# Golden Label: entailment

gum_pieces_premise = 54.0
gum_pieces_received_premise = 16.0
total_gum_pieces_hypothesis = 70.0

# the hypothesis talks about the total number of pieces of gum Todd has, which are also mentioned in the premise
# calculate the total number of gum pieces in the premise
total_gum_pieces_premise = gum_pieces_premise + gum_pieces_received_premise
if total_gum_pieces_hypothesis != total_gum_pieces_premise:
    # check if the total number of gum pieces in the hypothesis contradicts the total number of gum pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

