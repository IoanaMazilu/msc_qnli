# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:7? A.
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 7:7? A.
# Golden Label: entailment

ratio_premise = 2/7
ratio_hypothesis = 7/7

# the hypothesis talks about the ratio of distances between A to B and B to C
if ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # check if the ratio in the hypothesis equals the ratio given in the premise
    label = "entailment"
else:
    # the premise gives a specific ratio for the distances
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

