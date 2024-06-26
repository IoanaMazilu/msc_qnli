sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_rank_premise = 5

sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1
sevilla_rank_hypothesis = 5

# the hypothesis mentions the final score and the rank of Sevilla in La Liga, which are also mentioned in the premise
if sevilla_score_hypothesis!= sevilla_score_premise orzaragoza_score_hypothesis!= zaragoza_score_premise or sevilla_rank_hypothesis!= sevilla_rank_premise:
    # check if the final score or rank of Sevilla in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
