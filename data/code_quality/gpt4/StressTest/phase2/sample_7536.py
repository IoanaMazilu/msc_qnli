subjects_scores_premise = [40, 60, 70, 80, 80]
subjects_scores_hypothesis = [50, 60, 70, 80, 80]

# the hypothesis talks about the scores Reeya obtained in different subjects, referenced also in the premise
# we compare each subject score in the premise with the corresponding one in the hypothesis
for premise_score, hypothesis_score in zip(subjects_scores_premise, subjects_scores_hypothesis):
    if premise_score >= hypothesis_score:
        # check if any premise score contradicts the estimate of less than 'hypothesis_score'
        label = "contradiction"
        break
else:
    # the premise gives exact scores for each subject
    # any score less than the premise scores is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
