team_points_premise = 60
team_points_hypothesis = 60
jason_percentage_premise = 60
jason_percentage_hypothesis = 60

# the hypothesis refers to the number of points scored by the team and the percentage of points accounted for by Jason
if team_points_hypothesis >= team_points_premise:
    # check if the hypothesis value contradicts the number of points scored in the premise
    label = "contradiction"
elif jason_percentage_hypothesis!= jason_percentage_premise:
    # check if the percentage of points accounted for by Jason in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
