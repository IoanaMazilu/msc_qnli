points_premise = 15
points_hypothesis = 15
position_premise = 4
position_hypothesis = 4

# the hypothesis mentions the number of points and the position of West Brom, which are also mentioned in the premise
if points_hypothesis != points_premise:
    # check if the points in the hypothesis contradicts the points reported in the premise
    label = "contradiction"
elif position_hypothesis != position_premise:
    # check if the position from the hypothesis contradicts the position in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
