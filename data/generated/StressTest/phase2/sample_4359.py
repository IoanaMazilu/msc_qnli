# Premise: Reeya obtained 65, 67, 76, 80 and 95 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained more than 35, 67, 76, 80 and 95 out of 100 in different subjects, What will be the average.
# Golden Label: entailment

# Defining premise variables
score1_premise = 65
score2_premise = 67
score3_premise = 76
score4_premise = 80
score5_premise = 95

# Defining hypothesis variables
score1_hypothesis = 35
score2_hypothesis = 67
score3_hypothesis = 76
score4_hypothesis = 80
score5_hypothesis = 95

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if score1_hypothesis >= score1_premise:
    # check if the first score in the hypothesis contradicts the first score in the premise
    label = "contradiction"
elif score2_hypothesis != score2_premise or score3_hypothesis != score3_premise or score4_hypothesis != score4_premise or score5_hypothesis != score5_premise:
    # check if the rest of the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

