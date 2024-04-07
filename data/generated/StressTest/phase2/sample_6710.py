# Premise: Jason's team scored 60 points in a game basketball and he accounted for 60 percent of their points.
# Hypothesis: Jason's team scored less than 60 points in a game basketball and he accounted for 60 percent of their points.
# Golden Label: contradiction

team_points_premise = 60
team_points_hypothesis = 60
jason_points_percentage = 60 / 100

# the hypothesis refers to the number of points scored by Jason's team and Jason's contribution to those points
if team_points_hypothesis >= team_points_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives exact number of points for the team
    # any number of points less than 'team_points_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

