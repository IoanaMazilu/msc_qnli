# Define variables for the numerical entities in the premise and hypothesis
score_1_premise = 7
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4

# Extract all quantities as valid numbers
score_1_premise = int(score_1_premise)
score_2_premise = int(score_2_premise)
score_3_premise = int(score_3_premise)
score_4_premise = int(score_4_premise)
score_1_hypothesis = int(score_1_hypothesis)
score_2_hypothesis = int(score_2_hypothesis)
score_3_hypothesis = int(score_3_hypothesis)
score_4_hypothesis = int(score_4_hypothesis)

# Check if the hypothesis values contradict the premise
if score_1_hypothesis!= score_1_premise or score_2_hypothesis!= score_2_premise or score_3_hypothesis!= score_3_premise or score_4_hypothesis!= score_4_premise:
    label = "contradiction"
elif score_1_hypothesis <= score_1_premise and score_2_hypothesis <= score_2_premise and score_3_hypothesis <= score_3_premise and score_4_hypothesis <= score_4_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
