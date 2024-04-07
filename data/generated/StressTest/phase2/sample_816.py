# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:5? A.
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 3:5? A.
# Golden Label: entailment

ratio_premise = 2 / 5
ratio_hypothesis = 3 / 5

# The hypothesis refers to the ratio of distances between A to B and B to C, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # any ratio less than 'ratio_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

