# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 4:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3?
# Golden Label: neutral

ratio_premise = 4/3
ratio_hypothesis = 2/3

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

