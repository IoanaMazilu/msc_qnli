# Premise: Premier League leaders Manchester United survived a scare at third division Southampton before they scored a 2-1 win.
# Hypothesis: Manchester United come from behind to beat Southampton 2-1.
# Golden Label: entailment

man_u_score_premise = 2
southampton_score_premise = 1
man_u_score_hypothesis = 2
southampton_score_hypothesis = 1

# the hypothesis mentions the result of the game, which is also mentioned in the premise
# the hypothesis also implies that Manchester United was behind at some point, which can be inferred from the premise mentioning a "scare"
if man_u_score_hypothesis != man_u_score_premise:
    # check if the score of Manchester United in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif southampton_score_hypothesis != southampton_score_premise:
    # check if the score of Southampton from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

