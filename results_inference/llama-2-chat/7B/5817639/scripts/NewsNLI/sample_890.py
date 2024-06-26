record_premise = 11
win_away_premise = 21

# the hypothesis mentions the team's win in Moscow, which is also referenced in the premise
if record_hypothesis!= record_premise:
    # check if the team's record in the hypothesis contradicts the record in the premise
    label = "contradiction"
elif win_away_hypothesis!= win_away_premise:
    # check if the team's win away from home in the hypothesis contradicts the team's win away from home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
