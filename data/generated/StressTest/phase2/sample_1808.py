# Premise: Reeya obtained 55, 67, 76, 82 and 55 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained more than 55, 67, 76, 82 and 55 out of 100 in different subjects, What will be the average.
# Golden Label: contradiction

subject_scores_premise = [55, 67, 76, 82, 55]
min_score_hypothesis = 55

# the hypothesis refers to the scores Reeya obtained in the premise
if min(subject_scores_premise) < min_score_hypothesis:
    # check if the minimum score in the premise is less than the minimum score mentioned in the hypothesis
    label = "contradiction"
else:
    # the hypothesis only gives an estimate for the minimum score, without any specific values
    # any scores greater than or equal to 'min_score_hypothesis' are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

