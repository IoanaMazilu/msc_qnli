# defining the scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4]
scores_hypothesis = [7, 2, 3, 4]

# checking if the scores in the hypothesis contradict the scores in the premise
for i in range(len(scores_premise)):
    if scores_hypothesis[i] <= scores_premise[i]:
        label = "contradiction"
        break
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
