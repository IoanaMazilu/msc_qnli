average_score_premise = 0
average_score_hypothesis = 0

# Define the scores in the examination
score_english_premise = 76
score_mathematics_premise = 60
score_chemistry_premise = 72
score_biology_premise = 77
score_french_language_premise = 55
score_physics_premise = 85

score_english_hypothesis = 66
score_mathematics_hypothesis = 60
score_chemistry_hypothesis = 72
score_biology_hypothesis = 77
score_french_language_hypothesis = 55
score_physics_hypothesis = 85

# Calculate the average score for each subject in the hypothesis
average_score_hypothesis = (score_english_hypothesis + score_mathematics_hypothesis + score_chemistry_hypothesis + score_biology_hypothesis + score_french_language_hypothesis + score_physics_hypothesis) / 6

# Check if the average scores in the hypothesis contradict the average scores in the premise
if average_score_hypothesis!= average_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
