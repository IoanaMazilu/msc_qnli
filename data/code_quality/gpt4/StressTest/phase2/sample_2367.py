teams_premise = 2
teams_hypothesis = 5

# the hypothesis talks about the number of teams, which is also referenced in the premise
if teams_hypothesis < teams_premise:
    # check if the number of teams in the hypothesis contradicts the number of teams in the premise
    label = "contradiction"
else:
    # the premise and hypothesis both speak about the same scenario, so we can infer entailment
    label = "entailment"

print(label)
