ratio_premise = 2/3
ratio_hypothesis = 8/3

# the hypothesis refers to the ratio of distances between A to B and B to C, which is also mentioned in the premise
if ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is consistent with the ratio in the premise, we cannot entail the average speed of Murali from A to C
    label = "neutral"

print(label)
