# Premise: Calculate Tony'' s average score in an exam if he obtained the following marks 53, 87, 89, 80 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Tony'' s average score in an exam if he obtained the following marks more than 33, 87, 89, 80 and 78 out of 100 in different subjects.
# Golden Label: entailment

# defining scores obtained by Tony in different subjects as per the premise
score1_premise = 53
score2_premise = 87
score3_premise = 89
score4_premise = 80
score5_premise = 78

# defining scores obtained by Tony in different subjects as per the hypothesis
score1_hypothesis = 33
score2_hypothesis = 87
score3_hypothesis = 89
score4_hypothesis = 80
score5_hypothesis = 78

# calculating average score obtained by Tony as per the premise
average_score_premise = (score1_premise + score2_premise + score3_premise + score4_premise + score5_premise) / 5

# calculating average score obtained by Tony as per the hypothesis
average_score_hypothesis = (score1_hypothesis + score2_hypothesis + score3_hypothesis + score4_hypothesis + score5_hypothesis) / 5

# the hypothesis refers to the average score of Tony mentioned in the premise
if average_score_premise < average_score_hypothesis:
    # check if the 'average_score_hypothesis' contradicts the 'average_score_premise'
    label = "contradiction"
elif average_score_premise == average_score_hypothesis:
    # check if 'average_score_hypothesis' is the same as 'average_score_premise'
    label = "entailment"
else:
    # if 'average_score_premise' is more than 'average_score_hypothesis', then the premise does not contradict the hypothesis, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)

