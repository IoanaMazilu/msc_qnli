# Premise: Calculate Tony'' s average score in an exam if he obtained the following marks more than 33, 87, 89, 80 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Tony'' s average score in an exam if he obtained the following marks 53, 87, 89, 80 and 78 out of 100 in different subjects.
# Golden Label: neutral

score1_premise = 33
score1_hypothesis = 53
score2_premise = 87
score2_hypothesis = 87
score3_premise = 89
score3_hypothesis = 89
score4_premise = 80
score4_hypothesis = 80
score5_premise = 78
score5_hypothesis = 78

# the hypothesis refers to the scores in different subjects mentioned in the premise
if score1_hypothesis <= score1_premise:
    # check if the score1_hypothesis contradicts the estimate of more than 'score1_premise'
    label = "contradiction"
elif score2_hypothesis != score2_premise or score3_hypothesis != score3_premise or score4_hypothesis != score4_premise or score5_hypothesis != score5_premise:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score1
    # any score greater than 'score1_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

