# Scores in premise
score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_5_premise = 5

# Scores in hypothesis
score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4
score_5_hypothesis = 5

# The hypothesis refers to the scores Roslin got in the game, which are also mentioned in the premise
if score_1_hypothesis >= score_1_premise:
    # Check if the score of 1 in the hypothesis contradicts the premise
    label = "contradiction"
elif score_2_hypothesis >= score_2_premise:
    # Check if the score of 2 in the hypothesis contradicts the premise
    label = "contradiction"
elif score_3_hypothesis >= score_3_premise:
    # Check if the score of 3 in the hypothesis contradicts the premise
    label = "contradiction"
elif score_4_hypothesis >= score_4_premise:
    # Check if the score of 4 in the hypothesis contradicts the premise
    label = "contradiction"
elif score_5_hypothesis >= score_5_premise:
    # Check if the score of 5 in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If all the scores in the hypothesis are less than the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
