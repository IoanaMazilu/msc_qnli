team_score_premise = 60
team_score_hypothesis = 70
jason_score_percentage = 60

# the hypothesis talks about the total score of Jason's team and the percentage of points scored by Jason, both mentioned in the premise
if team_score_premise > team_score_hypothesis:
    # check if the team score in the premise contradicts the hypothesis estimate of less than 'team_score_hypothesis'
    label = "contradiction"
elif jason_score_percentage != 60:
    # check if the percentage of points scored by Jason in the premise contradicts the percentage mentioned in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
