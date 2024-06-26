team_score_premise = 60
team_score_hypothesis = 60
jason_points_premise = 60
jason_points_hypothesis = 60

# the hypothesis refers to the score of Jason's team and the points he accounted for, both mentioned in the premise
if team_score_hypothesis >= team_score_premise:
    # check if the estimate of 'team_score_hypothesis' contradicts the score of the team in the premise
    label = "contradiction"
elif jason_points_hypothesis!= jason_points_premise:
    # check if the percentage of points accounted for by Jason in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
