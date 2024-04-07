# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 3:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 6:3?
# Golden Label: neutral

# ratio of distances from A to B and B to C in the premise
distance_ratio_premise = 3 / 3

# ratio of distances from A to B and B to C in the hypothesis
distance_ratio_hypothesis = 6 / 3

# the hypothesis refers to the ratio of distances mentioned in the premise
if distance_ratio_hypothesis < distance_ratio_premise:
    # check if the ratio of distances in the hypothesis contradicts the premise estimate of more than 'distance_ratio_premise'
    label = "contradiction"
elif distance_ratio_hypothesis == distance_ratio_premise:
    # check if the ratio of distances in the hypothesis exactly equals the premise estimate, which is a contradiction since the premise states 'more than'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than 'distance_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

