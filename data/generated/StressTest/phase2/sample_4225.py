# Premise: In an exam, Amar scored more than 54 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored 84 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: neutral

amar_score_premise = 54
amar_score_hypothesis = 84
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis talks about the scores of Amar, Bhavan and Chetan in an exam, referenced also in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the hypothesis value for Amar contradicts the estimate of more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if the scores of Bhavan or Chetan in hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Amar's score
    # Any score greater than 'amar_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

