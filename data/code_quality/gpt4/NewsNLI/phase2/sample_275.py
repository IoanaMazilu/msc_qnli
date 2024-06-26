napoli_score_premise = 2
roma_score_premise = 2
napoli_score_hypothesis = 2
roma_score_hypothesis = 2

# the hypothesis mentions the draw score between Napoli and Roma in Serie A, which is also mentioned in the premise
if napoli_score_hypothesis != napoli_score_premise:
    # check if the Napoli's score in the hypothesis contradicts the Napoli's score reported in the premise
    label = "contradiction"
elif roma_score_hypothesis != roma_score_premise:
    # check if the Roma's score from the hypothesis contradicts the Roma's score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
