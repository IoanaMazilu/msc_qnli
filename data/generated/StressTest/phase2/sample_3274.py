# Premise: In an exam, Amar scored more than 14 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored 64 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: neutral

amar_score_premise = 14
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan in an exam, as mentioned in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the hypothesis value contradicts the premise that Amar scored more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise:
    # check if Bhavan's score in the hypothesis contradicts Bhavan's score in the premise
    label = "contradiction"
elif chetan_score_hypothesis != chetan_score_premise:
    # check if Chetan's score in the hypothesis contradicts Chetan's score in the premise
    label = "contradiction"
else:
    # Amar's score in the hypothesis is higher than 'amar_score_premise' which is consistent with the premise
    # but since the exact score is not provided in the premise, we cannot infer entailment
    label = "neutral"

print(label)

