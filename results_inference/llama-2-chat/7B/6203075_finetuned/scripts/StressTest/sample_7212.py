# Scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [less_than(8), 2, 3, 4, 5]

# Check if the scores in the hypothesis contradict the scores in the premise
if scores_premise!= scores_hypothesis:
    label = "contradiction"
else:
    # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
