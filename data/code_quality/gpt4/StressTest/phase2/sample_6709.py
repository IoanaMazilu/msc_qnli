team_score_premise = 70
team_score_hypothesis = 60
jason_points_percentage = 60

# the hypothesis refers to the team's score and Jason's contribution to it, mentioned in the premise
if team_score_hypothesis >= team_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'team_score_premise'
    label = "contradiction"
elif jason_points_percentage != 60:
    # check if the percentage of Jason's points in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the team's score
    # any team score less than 'team_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
