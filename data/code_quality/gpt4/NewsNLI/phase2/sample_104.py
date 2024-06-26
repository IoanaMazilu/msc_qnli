monaco_score_premise = 1
guingamp_score_premise = 1
monaco_score_hypothesis = 1
guingamp_score_hypothesis = 1

# the hypothesis mentions the score of the Monaco vs Guingamp match, which is also referenced in the premise
if monaco_score_hypothesis != monaco_score_premise or guingamp_score_hypothesis != guingamp_score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
