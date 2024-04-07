# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 8:4?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 4:4?
# Golden Label: entailment

ratio_premise = 8/4
ratio_hypothesis = 4/4

# the hypothesis discusses the average speed of Murali from A to C based on the ratio of distances between A to B and B to C
# this is also discussed in the premise.
if ratio_hypothesis < ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # check if the ratio in the hypothesis is the same as the ratio given in the premise
    label = "entailment"
else:
    # the premise gives a specific ratio for the distances between A to B and B to C
    # any ratio greater than the 'ratio_premise' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

