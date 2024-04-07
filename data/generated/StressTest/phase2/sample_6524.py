# Premise: Reeya obtained 55, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 35, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Golden Label: contradiction

# variables for the scores obtained by Reeya in different subjects
reeya_scores_premise = [55, 67, 76, 82, 85]
reeya_scores_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if reeya_scores_premise != reeya_scores_hypothesis:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)

