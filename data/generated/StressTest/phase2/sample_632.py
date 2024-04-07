# Premise: In an exam, Amar scored 64 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Hypothesis: In an exam, Amar scored 54 percent, Bhavan scored 36 percent and Chetan 44 percent.
# Golden Label: contradiction

amar_score_premise = 64
amar_score_hypothesis = 54
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis mentions the scores of Amar, Bhavan and Chetan which are also mentioned in the premise
if amar_score_premise != amar_score_hypothesis:
    # check if the score of Amar in the hypothesis contradicts the score of Amar in the premise
    label = "contradiction"
elif bhavan_score_premise != bhavan_score_hypothesis:
    # check if the score of Bhavan in the hypothesis contradicts the score of Bhavan in the premise
    label = "contradiction"
elif chetan_score_premise != chetan_score_hypothesis:
    # check if the score of Chetan in the hypothesis contradicts the score of Chetan in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

