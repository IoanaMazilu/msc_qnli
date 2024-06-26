team_score_premise = 60
team_score_hypothesis = 60
jason_percentage_premise = 60
jason_percentage_hypothesis = 60

# the hypothesis refers to the team score and Jason's percentage of points mentioned in the premise
if team_score_hypothesis >= team_score_premise:
    # check if the estimate of 'team_score_hypothesis' contradicts the team score in the premise
    label = "contradiction"
elif jason_percentage_hypothesis!= jason_percentage_premise:
    # check if the percentage of points in the hypothesis contradicts the percentage of points reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
