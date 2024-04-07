# Premise: Reeya obtained 50, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained less than 50, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Golden Label: contradiction

# Scores obtained by Reeya in different subjects in the premise
score1_premise = 50
score2_premise = 60
score3_premise = 70
score4_premise = 80
score5_premise = 80

# Scores obtained by Reeya in different subjects in the hypothesis
score1_hypothesis = 50
score2_hypothesis = 60
score3_hypothesis = 70
score4_hypothesis = 80
score5_hypothesis = 80

# Compare each score in the hypothesis with the corresponding score in the premise
if score1_hypothesis >= score1_premise or score2_hypothesis >= score2_premise or score3_hypothesis >= score3_premise or score4_hypothesis >= score4_premise or score5_hypothesis >= score5_premise:
    # If any score in the hypothesis is greater than or equal to the corresponding score in the premise,
    # then the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If all scores in the hypothesis are less than the corresponding scores in the premise,
    # then the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)

