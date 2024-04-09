points_scored_premise = 60
points_scored_hypothesis = 60
percentage_premise = 60
percentage_hypothesis = 60

# the hypothesis refers to the points scored by Jason's team and the percentage of points he accounted for, both mentioned in the premise
if points_scored_hypothesis >= points_scored_premise:
    # check if the estimate of 'points_scored_hypothesis' contradicts the number of points scored in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of points accounted for in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
