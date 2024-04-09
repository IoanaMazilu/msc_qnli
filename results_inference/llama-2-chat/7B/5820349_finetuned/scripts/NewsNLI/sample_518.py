bayern_score_premise = 2
hannover_score_premise = 0
bayern_score_hypothesis = 2
hannover_score_hypothesis = 0

# the hypothesis mentions the score of Bayern Munich's game against Hannover, which is also mentioned in the premise
if bayern_score_hypothesis!= bayern_score_premise:
    # check if the Bayern Munich's score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif hannover_score_hypothesis!= hannover_score_premise:
    # check if the Hannover's score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
