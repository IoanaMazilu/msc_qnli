subject_scores_premise = [35, 67, 76, 80, 95]  # Scores obtained by Reeya in different subjects according to the premise
subject_scores_hypothesis = [65, 67, 76, 80, 95]  # Scores obtained by Reeya in different subjects according to the hypothesis

# the hypothesis talks about the scores obtained by Reeya in different subjects, referenced also in the premise
if min(subject_scores_hypothesis) <= min(subject_scores_premise):
    # check if the lowest score obtained by Reeya in the hypothesis contradicts the premise stating she obtained more than 35 in different subjects
    label = "contradiction"
else:
    # the premise gives only a minimum value for the scores obtained by Reeya
    # any score greater than 35 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)
