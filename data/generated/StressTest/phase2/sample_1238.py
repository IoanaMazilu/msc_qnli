# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 8:4?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 7:4?
# Golden Label: contradiction

distance_ratio_premise_AB_BC = [8, 4]
distance_ratio_hypothesis_AB_BC = [7, 4]

# the hypothesis changes the ratio of distances mentioned in the premise
if distance_ratio_hypothesis_AB_BC != distance_ratio_premise_AB_BC:
    # check if any of the ratios in the hypothesis contradicts the ratios mentioned in the premise
    label = "contradiction"
else:
    # the ratios are identical
    label = "entailment"

print(label)

