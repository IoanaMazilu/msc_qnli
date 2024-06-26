lowest_score_premise = 1
lowest_score_hypothesis = 1

# The hypothesis refers to the scores Mary got in the game, which is also mentioned in the premise
if lowest_score_hypothesis != lowest_score_premise:
    # Check if the minimum score in the hypothesis contradicts the minimum score in the premise
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
