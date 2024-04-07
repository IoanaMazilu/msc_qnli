# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 6:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 3:3?
# Golden Label: contradiction

dist_ratio_premise = 6/3
dist_ratio_hypothesis = 3/3

# The hypothesis refers to the ratio of distances from A to B and B to C, which is also mentioned in the premise
if dist_ratio_hypothesis != dist_ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # If the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

