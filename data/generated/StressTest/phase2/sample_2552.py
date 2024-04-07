# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 5:3?
# Golden Label: contradiction

ratio_distances_premise = [2, 3]
ratio_distances_hypothesis = [5, 3]

# the hypothesis talks about the ratio of distances between A to B and B to C, which is also referenced in the premise
if ratio_distances_premise != ratio_distances_hypothesis:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # if the ratio of distances in the hypothesis does not contradict the ratio of distances in the premise, we can infer entailment
    label = "entailment"

print(label)

