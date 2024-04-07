# Premise: Mary played the game, getting at least one score of each of 1, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Hypothesis: Mary played the game, getting at least one score of each of 2, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Golden Label: contradiction

scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [2, 2, 3, 4, 5]

# The hypothesis talks about the scores Mary got in the game, referenced also in the premise
# Check if each score in the hypothesis is also in the premise
for score in scores_hypothesis:
    if score not in scores_premise:
        label = "contradiction"
        break
else:
    # The premise and hypothesis specify the same condition about not getting the same score in consecutive steps
    # If the hypothesis scores are all in the premise scores, we can infer entailment
    label = "entailment"

print(label)

