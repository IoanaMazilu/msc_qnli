# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 1:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 3:3?
# Golden Label: neutral

ratio_premise = 1/3
ratio_hypothesis = 3/3

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_hypothesis != ratio_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

