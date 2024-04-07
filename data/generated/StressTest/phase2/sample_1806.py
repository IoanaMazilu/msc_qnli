# Premise: Reeya obtained 55, 67, 76, 82 and 55 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained less than 85, 67, 76, 82 and 55 out of 100 in different subjects, What will be the average.
# Golden Label: entailment

# The premise and hypothesis are about Reeya's score in different subjects

# Scores from premise
score1_premise = 55
score2_premise = 67
score3_premise = 76
score4_premise = 82
score5_premise = 55

# Scores from hypothesis
score1_hypothesis = 85
score2_hypothesis = 67
score3_hypothesis = 76
score4_hypothesis = 82
score5_hypothesis = 55

# Checking if all scores from hypothesis are less or equal than scores from premise
if (score1_hypothesis <= score1_premise and score2_hypothesis <= score2_premise and
    score3_hypothesis <= score3_premise and score4_hypothesis <= score4_premise and
    score5_hypothesis <= score5_premise):
    label = "entailment"
# Checking if any score from hypothesis is more than score from premise
elif (score1_hypothesis > score1_premise or score2_hypothesis > score2_premise or
      score3_hypothesis > score3_premise or score4_hypothesis > score4_premise or
      score5_hypothesis > score5_premise):
    label = "contradiction"
else:
    # If there is no contradiction and no full entailment, then the relation is neutral
    label = "neutral"

print(label)

