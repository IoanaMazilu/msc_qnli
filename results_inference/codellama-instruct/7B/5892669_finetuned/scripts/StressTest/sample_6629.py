# Scores in the premise
score1_premise = 1
score2_premise = 2
score3_premise = 3

# Scores in the hypothesis
score1_hypothesis = 1
score2_hypothesis = 2
score3_hypothesis = 3

# The hypothesis refers to the scores Mary got in the game, which are also mentioned in the premise
if score1_hypothesis >= score1_premise or score2_hypothesis >= score2_premise or score3_hypothesis >= score3_premise:
    # Check if the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
