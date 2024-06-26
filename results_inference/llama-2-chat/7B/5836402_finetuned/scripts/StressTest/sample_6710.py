points_scored_premise = 60
points_scored_hypothesis = 60
jason_points_premise = 60
jason_points_hypothesis = 60

# the hypothesis talks about the points scored by Jason's team and his percentage, which are also mentioned in the premise
if points_scored_hypothesis >= points_scored_premise:
    # check if the hypothesis value contradicts the number of points scored by Jason's team in the premise
    label = "contradiction"
elif jason_points_hypothesis!= jason_points_premise:
    # check if the percentage of points accounted by Jason in the hypothesis contradicts the percentage of points accounted by Jason in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
