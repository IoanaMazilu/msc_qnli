# Scores in premise and hypothesis
score_premise = [7, 2, 3, 4]
score_hypothesis = [1, 2, 3, 4]

# Check if the scores in the hypothesis contradict the scores in the premise
for i in range(len(score_hypothesis)):
    if score_hypothesis[i] >= score_premise[i]:
        label = "contradiction"
        break
else:
    # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
