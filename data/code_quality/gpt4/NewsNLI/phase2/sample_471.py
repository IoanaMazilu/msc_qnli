score_premise = (5, 1) # Real Madrid's score vs Real Murcia's score
score_hypothesis = (5, 1) # Real Madrid's score vs Real Murcia's score

# the hypothesis mentions the match's score between Real Madrid and Real Murcia, which is also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the match's score in the hypothesis contradicts the match's score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
