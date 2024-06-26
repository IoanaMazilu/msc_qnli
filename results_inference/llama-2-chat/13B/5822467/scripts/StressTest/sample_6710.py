jason_team_points_premise = 60
jason_team_points_hypothesis = 50
jason_percentage_premise = 60

# the hypothesis refers to the number of points scored by Jason's team and the percentage of points accounted for by Jason
if jason_team_points_hypothesis <= jason_team_points_premise:
    # check if the estimate of 'jason_team_points_hypothesis' contradicts the number of points scored by Jason's team in the premise
    label = "contradiction"
elif jason_percentage_premise!= jason_percentage_hypothesis:
    # check if the percentage of points accounted for by Jason in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
