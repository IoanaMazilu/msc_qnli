points_premise = 14
points_hypothesis = 14

# the hypothesis mentions the number of points Webber has in the world title race, which is also mentioned in the premise
if points_hypothesis!= points_premise:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
