score1_premise = 6
score2_premise = 3
score3_premise = 6
score4_premise = 4

score1_hypothesis = 6
score2_hypothesis = 3
score3_hypothesis = 6
score4_hypothesis = 4

# the hypothesis mentions the scores of the game, which are also mentioned in the premise
if score1_hypothesis != score1_premise or score2_hypothesis != score2_premise or score3_hypothesis != score3_premise or score4_hypothesis != score4_premise:
    # check if any of the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
