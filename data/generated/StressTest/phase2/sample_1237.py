# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 4:4?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 8:4?
# Golden Label: neutral

ratio_premise = 4/4
ratio_hypothesis = 8/4

# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

