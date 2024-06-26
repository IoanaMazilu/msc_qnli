# Scores obtained by Reeya in different subjects according to the premise and hypothesis
scores_premise = [55, 67, 76, 82, 85]
scores_hypothesis = [35, 67, 76, 82, 85]

# Check if the scores obtained in the hypothesis contradict the scores obtained in the premise
if scores_premise!= scores_hypothesis:
    label = "contradiction"
else:
    # If the scores obtained in the hypothesis do not contradict the scores obtained in the premise, we can infer entailment
    label = "entailment"

print(label)
