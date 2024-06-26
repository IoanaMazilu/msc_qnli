# Define the scores of each subject
english_score = 66
mathematics_score = 60
chemistry_score = 72
biology_score = 77
french_score = 55
physics_score = 85

# Define the hypothesis
hypothesis_score_english = 76
hypothesis_score_mathematics = 60
hypothesis_score_chemistry = 72
hypothesis_score_biology = 77
hypothesis_score_french = 55
hypothesis_score_physics = 85

# Calculate the average score of each subject in the hypothesis
hypothesis_average_score_english = (hypothesis_score_english / 1) if hypothesis_score_english < 76 else 0
hypothesis_average_score_mathematics = (hypothesis_score_mathematics / 1) if hypothesis_score_mathematics < 60 else 0
hypothesis_average_score_chemistry = (hypothesis_score_chemistry / 1) if hypothesis_score_chemistry < 72 else 0
hypothesis_average_score_biology = (hypothesis_score_biology / 1) if hypothesis_score_biology < 77 else 0
hypothesis_average_score_french = (hypothesis_score_french / 1) if hypothesis_score_french < 55 else 0
hypothesis_average_score_physics = (hypothesis_score_physics / 1) if hypothesis_score_physics < 85 else 0

# Check if the hypothesis scores contradict the premise scores
if hypothesis_average_score_english!= english_score or hypothesis_average_score_mathematics!= mathematics_score or hypothesis_average_score_chemistry!= chemistry_score or hypothesis_average_score_biology!= biology_score or hypothesis_average_score_french!= french_score or hypothesis_average_score_physics!= physics_score:
    label = "contradiction"
else:
    label = "entailment"

print(label)
