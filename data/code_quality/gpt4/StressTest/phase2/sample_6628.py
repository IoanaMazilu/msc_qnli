score_premise = 8
score_hypothesis = 1

# The hypothesis refers to the scores Mary got in the game, which are also mentioned in the premise
if score_hypothesis >= score_premise:
    # Check if the score in the hypothesis contradicts the condition of less than 'score_premise' in the premise
    label = "contradiction"
elif score_hypothesis > 3:
    # Check if the score in the hypothesis contradicts the explicit scores of 2 and 3 mentioned in the premise
    label = "contradiction"
else:
    # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
