# Premise: Reeya obtained 65, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 15, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Golden Label: contradiction

# Scores obtained by Reeya in different subjects according to the premise and hypothesis
scores_premise = [65, 67, 76, 82, 85]
scores_hypothesis = [15, 67, 76, 82, 85]

# Check if the scores obtained in the hypothesis contradict the scores obtained in the premise
if scores_premise != scores_hypothesis:
    label = "contradiction"
else:
    # The hypothesis does not provide any additional information or contradict the premise
    label = "neutral"

print(label)

