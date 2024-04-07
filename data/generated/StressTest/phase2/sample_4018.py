# Premise: Calculate Ronald's average score in an exam if he obtained the following marks more than 21, 57, 68, 60 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Ronald's average score in an exam if he obtained the following marks 51, 57, 68, 60 and 78 out of 100 in different subjects.
# Golden Label: neutral

# defining variables for the scores
score1_premise = 21
score2_premise = 57
score3_premise = 68
score4_premise = 60
score5_premise = 78

score1_hypothesis = 51
score2_hypothesis = 57
score3_hypothesis = 68
score4_hypothesis = 60
score5_hypothesis = 78

# calculating the average scores for premise and hypothesis
average_score_premise = (score1_premise + score2_premise + score3_premise + score4_premise + score5_premise) / 5
average_score_hypothesis = (score1_hypothesis + score2_hypothesis + score3_hypothesis + score4_hypothesis + score5_hypothesis) / 5

# the hypothesis talks about the average score of Ronald, similarly referred in the premise
if average_score_premise < average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the premise condition of scores being more than 21, 57, 68, 60 and 78
    label = "contradiction"
elif average_score_premise == average_score_hypothesis:
    # if the average score in the hypothesis equals the average score in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a condition for the individual scores, not the average
    # any average score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

