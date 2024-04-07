# Premise: Reeya obtained 65, 67, 76, 80 and 95 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 85, 67, 76, 80 and 95 out of 100 in different subjects, What will be the average.
# Golden Label: contradiction

# Scores obtained by Reeya in different subjects according to the premise
scores_premise = [65, 67, 76, 80, 95]

# Scores obtained by Reeya in different subjects according to the hypothesis
scores_hypothesis = [85, 67, 76, 80, 95]

# Check if the scores in premise and hypothesis are equal
if scores_premise == scores_hypothesis:
    label = "entailment"
else:
    # The premise and hypothesis contradict each other
    label = "contradiction"

print(label)

