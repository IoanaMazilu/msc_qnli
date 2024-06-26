points_premise = 3
points_hypothesis = 3
goal_difference_premise = 0
goal_difference_hypothesis = 0

# the hypothesis mentions the number of points and goal difference in Ecuador, which are also mentioned in the premise
if points_hypothesis!= points_premise:
    # check if the number of points from the hypothesis contradicts the number of points in the premise
    label = "contradiction"
elif goal_difference_hypothesis!= goal_difference_premise:
    # check if the goal difference from the hypothesis contradicts the goal difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
