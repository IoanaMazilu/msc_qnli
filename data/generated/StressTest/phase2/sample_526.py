# Premise: In an exam, Amar scored less than 74 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored 64 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: neutral

amar_score_premise = 74
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan mentioned in the premise
if amar_score_hypothesis >= amar_score_premise:
    # check if Amar's score in the hypothesis contradicts the estimate of less than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if Bhavan's or Chetan's score in the hypothesis contradicts the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
