# Premise: In an exam, Amar scored 64 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored less than 84 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: entailment

amar_score_premise = 64
bhavan_score_premise = 36
chetan_score_premise = 44

amar_score_hypothesis = 84
bhavan_score_hypothesis = 36
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_premise >= amar_score_hypothesis:
    # check if the estimate of 'amar_score_hypothesis' contradicts the score of Amar in the premise
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if the scores of Bhavan and Chetan in the hypothesis contradict the scores of Bhavan and Chetan in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

