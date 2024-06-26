season_premise = 28
season_hypothesis = 28

# the season in the premise and the hypothesis are the same
if season_hypothesis!= season_premise:
    # check if the season in the hypothesis contradicts the season in the premise
    label = "contradiction"
else:
    # if the season in the hypothesis does not contradict the season in the premise, we can infer entailment
    label = "entailment"

print(label)
