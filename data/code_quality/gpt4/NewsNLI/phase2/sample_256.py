pearce_vote_percentage_premise = 45.3
pearce_vote_percentage_hypothesis = 45.3

# the hypothesis mentions the vote percentage of Pearce, which is also referenced in the premise
if pearce_vote_percentage_hypothesis != pearce_vote_percentage_premise:
    # check if the vote percentage in the hypothesis contradicts the vote percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
