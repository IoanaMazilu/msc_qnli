score_premise = 3
score_hypothesis = 3
team1_premise = "Sevilla"
team2_premise = "Real Zaragoza"
team1_hypothesis = "Sevilla"
team2_hypothesis = "Real Zaragoza"

# the hypothesis mentions the score and the teams, which are also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif team1_hypothesis!= team1_premise or team2_hypothesis!= team2_premise:
    # check if the team names in the hypothesis contradict the team names reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and team names do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
