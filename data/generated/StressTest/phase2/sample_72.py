# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3? A.
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 6:3? A.
# Golden Label: entailment

ratio_premise = 2/3
ratio_hypothesis = 6/3

# the hypothesis refers to the ratio of distances between A to B and B to C as in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)

