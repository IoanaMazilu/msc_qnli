# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is more than 1:2?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 4:2?
# Golden Label: neutral

ratio_premise = 1/2
ratio_hypothesis = 4/2

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the value of 'ratio_hypothesis' contradicts the estimate in the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # check if the value of 'ratio_hypothesis' is consistent with the estimate in the premise
    # however, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

