# Premise: Reeya obtained 55, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained more than 45, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Golden Label: entailment

# scores obtained by Reeya in different subjects in the premise
rey_scores_premise = [55, 67, 76, 82, 85]
# scores obtained by Reeya in different subjects in the hypothesis
rey_scores_hypothesis = [45, 67, 76, 82, 85]

# we compare the scores one by one between the premise and the hypothesis
for score_premise, score_hypothesis in zip(rey_scores_premise, rey_scores_hypothesis):
    if score_premise != score_hypothesis:
        # if a score in the hypothesis is not the same as the score in the premise
        # it contradicts the premise
        label = "contradiction"
        break
else:
    # if all the scores in the hypothesis are the same as the scores in the premise
    # it is consistent with the premise
    label = "entailment"

print(label)

