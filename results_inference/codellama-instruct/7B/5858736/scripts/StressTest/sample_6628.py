# Define variables for the numerical entities in the premise and hypothesis
score_less_than_8_premise = 8
score_2_premise = 2
score_3_premise = 3
score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3

# Extract all quantities as valid numbers
score_less_than_8_premise = int(score_less_than_8_premise)
score_2_premise = int(score_2_premise)
score_3_premise = int(score_3_premise)
score_1_hypothesis = int(score_1_hypothesis)
score_2_hypothesis = int(score_2_hypothesis)
score_3_hypothesis = int(score_3_hypothesis)

# Check if the hypothesis values contradict the premise
if score_1_hypothesis!= score_2_premise or score_2_hypothesis!= score_3_premise or score_3_hypothesis!= score_less_than_8_premise:
    label = "contradiction"
elif score_1_hypothesis == score_2_premise and score_2_hypothesis == score_3_premise and score_3_hypothesis == score_less_than_8_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
