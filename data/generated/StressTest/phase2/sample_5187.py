# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 6:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 3:3?
# Golden Label: entailment

ratio_distances_premise = 6/3
ratio_distances_hypothesis = 3/3

# the hypothesis talks about the ratio of distances between A to B and B to C, which is also mentioned in the premise
if ratio_distances_hypothesis >= ratio_distances_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances given in the premise
    label = "contradiction"
else:
    # if the ratio of distances in the hypothesis does not contradict the ratio of distances given in the premise, we can infer entailment
    label = "entailment"

print(label)

